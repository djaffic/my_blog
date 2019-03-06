from django.db import models
from django.urls import reverse


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

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
