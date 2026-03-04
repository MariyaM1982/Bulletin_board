from rest_framework import viewsets

from ads.serializers import UserSerializer

from .models import User


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для пользователя."""

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        """Возвращает список пользователей."""
        if self.request.user.is_staff:
            return User.objects.all()
        return User.objects.none()  # или только публичные данные
