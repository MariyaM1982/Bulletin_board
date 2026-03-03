from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Разрешает редактирование/удаление только владельцу.
    Админ может всё.
    """
    def has_object_permission(self, request, view, obj):
        # Все могут читать
        if request.method in permissions.SAFE_METHODS:
            return True

        # Администратор может редактировать/удалять любые объекты
        if request.user.is_staff:
            return True

        # Иначе — только владелец
        return obj.author == request.user


class IsReviewAuthorOrReadOnly(permissions.BasePermission):
    """
    Позволяет редактировать/удалять только автору отзыва.
    Админ может всё.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_staff:
            return True

        return obj.author == request.user