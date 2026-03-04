from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Админка для модели User."""

    # Поля, отображаемые в списке пользователей
    list_display = ("email", "first_name", "last_name", "role", "is_active", "is_staff")
    list_filter = ("is_active", "is_staff", "role")
    search_fields = ("email", "first_name", "last_name")

    # Поля при редактировании
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Персональная информация",
            {"fields": ("first_name", "last_name", "phone", "image")},
        ),
        ("Права", {"fields": ("role", "is_active", "is_staff", "is_superuser")}),
        ("Важные даты", {"fields": ("last_login", "date_joined")}),
    )

    # Поля при создании
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "role",
                    "first_name",
                    "last_name",
                    "phone",
                ),
            },
        ),
    )

    ordering = ("email",)
    filter_horizontal = ()

    # Отключаем username
    def get_form(self, request, obj=None, **kwargs):
        """Отключает поле username."""
        form = super().get_form(request, obj, **kwargs)
        if "username" in form.base_fields:
            form.base_fields.pop("username")
        return form
