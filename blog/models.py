from django.db import models


class Post(models.Model):
    """Модель статьи"""
    title = models.CharField("Название статьи", max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        verbose_name="Автор"
    )
    body = models.TextField()

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title
