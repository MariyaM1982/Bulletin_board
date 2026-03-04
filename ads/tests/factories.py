import factory

from ads.models import Ad, Review
from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Sequence(lambda n: f"user{n}@example.com")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    phone = factory.Sequence(lambda n: f"+790000000{n:02d}")
    role = "member"
    password = factory.PostGenerationMethodCall("set_password", "password123")


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    title = factory.Faker("sentence", nb_words=4)
    price = factory.Faker("random_int", min=1000, max=100000)
    description = factory.Faker("text")
    author = factory.SubFactory(UserFactory)


class ReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Review

    text = factory.Faker("paragraph")
    ad = factory.SubFactory(AdFactory)
    author = factory.SubFactory(UserFactory)
