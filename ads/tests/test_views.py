import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from ads.models import Ad, Review

from .factories import AdFactory, ReviewFactory, UserFactory


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def admin_user():
    return UserFactory(is_staff=True)


@pytest.fixture
def ad():
    return AdFactory()


@pytest.mark.django_db
class TestAdViews:
    """Тесты для объявлений."""

    def test_list_ads(self, api_client):
        """Тест получения списка объявлений."""
        AdFactory.create_batch(5)
        url = reverse("ad-list")
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 4  # пагинация

    def test_create_ad_authenticated(self, api_client, user):
        """Тест создания объявления авторизованным пользователем."""
        api_client.force_authenticate(user=user)
        url = reverse("ad-list")
        data = {"title": "Ноутбук", "price": 25000, "description": "Отличное состояние"}
        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Ad.objects.count() == 1
        assert Ad.objects.first().author == user

    def test_create_ad_unauthenticated(self, api_client):
        """Тест создания объявления неавторизованным пользователем."""
        url = reverse("ad-list")
        data = {"title": "Телефон", "price": 15000}
        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_update_ad_owner(self, api_client, user):
        """Тест обновления объявления владельцем."""
        ad = AdFactory(author=user)
        api_client.force_authenticate(user=user)
        url = reverse("ad-detail", kwargs={"pk": ad.id})
        data = {"title": "Обновлённый ноутбук"}
        response = api_client.patch(url, data)
        assert response.status_code == status.HTTP_200_OK
        ad.refresh_from_db()
        assert ad.title == "Обновлённый ноутбук"

    def test_update_ad_other_user(self, api_client, user):
        """Тест обновления объявления не владельцем."""
        other_user = UserFactory()
        ad = AdFactory(author=other_user)
        api_client.force_authenticate(user=user)
        url = reverse("ad-detail", kwargs={"pk": ad.id})
        data = {"title": "Не мой ноутбук"}
        response = api_client.patch(url, data)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_admin_can_delete_any_ad(self, api_client, admin_user):
        """Тест удаления объявления администратором."""
        other_user = UserFactory()
        ad = AdFactory(author=other_user)
        api_client.force_authenticate(user=admin_user)
        url = reverse("ad-detail", kwargs={"pk": ad.id})
        response = api_client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
class TestReviewViews:
    """Тесты для отзывов."""

    def test_create_review_authenticated(self, api_client, user, ad):
        """Тест создания отзыва авторизованным пользователем."""
        api_client.force_authenticate(user=user)
        url = reverse("review-list")
        data = {"text": "Хороший товар!", "ad": ad.id}
        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Review.objects.count() == 1

    def test_user_can_edit_own_review(self, api_client, user):
        """Тест редактирования собственного отзыва."""
        review = ReviewFactory(author=user)
        api_client.force_authenticate(user=user)
        url = reverse("review-detail", kwargs={"pk": review.id})
        data = {"text": "Обновил отзыв"}
        response = api_client.patch(url, data)
        assert response.status_code == status.HTTP_200_OK
        review.refresh_from_db()
        assert review.text == "Обновил отзыв"

    def test_user_cannot_edit_other_review(self, api_client, user):
        """Тест редактирования чужого отзыва."""
        other_user = UserFactory()
        review = ReviewFactory(author=other_user)
        api_client.force_authenticate(user=user)
        url = reverse("review-detail", kwargs={"pk": review.id})
        data = {"text": "Хочу взломать"}
        response = api_client.patch(url, data)
        assert response.status_code == status.HTTP_403_FORBIDDEN
