from rest_framework import serializers
from .models import Ad, Review
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'phone', 'role')


class AdSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Ad
        fields = (
            'id',
            'title',
            'price',
            'description',
            'author',
            'created_at',
        )
        read_only_fields = ('created_at', 'author')


# Добавлено: AdListSerializer
class AdListSerializer(AdSerializer):
    class Meta(AdSerializer.Meta):
        fields = ('id', 'title', 'price', 'author', 'created_at')


class ReviewSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'ad', 'created_at')
        read_only_fields = ('author', 'created_at')