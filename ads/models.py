from django.db import models

from users.models import User


class Ad(models.Model):
    """Объявление, публикуемое пользователем.

    Содержит заголовок, цену, описание и ссылку на автора.
    Используется для торговли товарами или услугами.
    """

    title = models.CharField("Название товара", max_length=200)
    price = models.PositiveIntegerField("Цена товара")  # Целое число, без копеек
    description = models.TextField("Описание товара", blank=True)
    author = models.ForeignKey(
        User,
        verbose_name="Автор объявления",
        on_delete=models.CASCADE,
        related_name="ads",
    )
    created_at = models.DateTimeField("Дата и время создания", auto_now_add=True)

    class Meta:
        """Настройки отображения модели в админ-панели."""

        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ["-created_at"]  # Сортировка: новые сверху

    def __str__(self):
        """Возвращает заголовок объявления."""
        return self.title


class Review(models.Model):
    """Отзыв на объявление.

    Может быть оставлен любым зарегистрированным пользователем.
    Только автор отзыва может его редактировать.
    """

    text = models.TextField("Текст отзыва")
    author = models.ForeignKey(
        User,
        verbose_name="Автор отзыва",
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    ad = models.ForeignKey(
        Ad, verbose_name="Объявление", on_delete=models.CASCADE, related_name="reviews"
    )
    created_at = models.DateTimeField("Дата и время создания", auto_now_add=True)

    class Meta:
        """Настройки отображения модели в админ-панели."""

        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ["created_at"]

    def __str__(self):
        """Возвращает начало текста отзыва."""
        return f"Отзыв от {self.author.email} на '{self.ad.title}'"
