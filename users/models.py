from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    """Менеджер для кастомной модели пользователя."""

    def create_user(self, email, password=None, **extra_fields):
        """Создает и возвращает пользователя с email и паролем."""
        if not email:
            raise ValueError("Email обязателен")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Создает и возвращает пользователя с привилегиями суперадмина."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", "admin")

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """Кастомная модель пользователя.

    Использует email как основной идентификатор.
    Поле username не используется.
    """

    ROLE_CHOICES = (
        ("user", "Пользователь"),
        ("admin", "Администратор"),
    )

    username = None  # отключаем стандартный username
    first_name = models.CharField("Имя", max_length=150)
    last_name = models.CharField("Фамилия", max_length=150)
    phone = models.CharField("Телефон", max_length=20, blank=True)
    email = models.EmailField("Email", unique=True)
    role = models.CharField("Роль", max_length=10, choices=ROLE_CHOICES, default="user")
    image = models.ImageField("Аватар", upload_to="users/", blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        """Возвращает email пользователя."""
        return self.email
