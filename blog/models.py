from django.conf import settings
from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое статьи')
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True, verbose_name='Изображение')
    views = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог пост'
        verbose_name_plural = 'Блог посты'
