from django.db import models

from users.models import User


class Ad(models.Model):
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
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ["-created_at"]  # Сортировка: новые сверху

    def __str__(self):
        return self.title


class Review(models.Model):
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
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ["created_at"]

    def __str__(self):
        return f"Отзыв от {self.author.email} на '{self.ad.title}'"
