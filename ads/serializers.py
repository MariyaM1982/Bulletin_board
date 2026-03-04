from rest_framework import serializers

from users.models import User

from .models import Ad, Review


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор модели User."""

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email", "phone", "role")


class AdSerializer(serializers.ModelSerializer):
    """Сериализатор модели Ad."""

    author = UserSerializer(read_only=True)

    class Meta:
        """Настройки отображения модели в админ-панели."""

        model = Ad
        fields = (
            "id",
            "title",
            "price",
            "description",
            "author",
            "created_at",
        )
        read_only_fields = ("created_at", "author")


# Добавлено: AdListSerializer
class AdListSerializer(AdSerializer):
    """Сериализатор модели Ad для списка объявлений."""

    class Meta(AdSerializer.Meta):
        """Настройки отображения модели в админ-панели."""

        fields = ("id", "title", "price", "author", "created_at")


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор модели Review."""

    author = UserSerializer(read_only=True)

    class Meta:
        """Настройки отображения модели в админ-панели."""

        model = Review
        fields = ("id", "text", "author", "ad", "created_at")
        read_only_fields = ("author", "created_at")
