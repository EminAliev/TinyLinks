from django.db import models


class Link(models.Model):
    full_link = models.CharField(max_length=200, verbose_name='Оригинальная ссылка')
    short_link = models.CharField(max_length=50, unique=True, verbose_name='Короткая ссылка')
    redirects = models.IntegerField(default=0, verbose_name='Редиректы')

    def __str__(self):
        return self.short_link

    class Meta:
        verbose_name = 'Ссылки'
        verbose_name_plural = 'Ссылки'
