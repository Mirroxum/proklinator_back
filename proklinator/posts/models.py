from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=512, verbose_name="Имя цели")
    curse = models.CharField(max_length=256, verbose_name="Проклятье")
    comment = models.CharField(max_length=512, null=True, verbose_name="Комментарий")
    duration = models.IntegerField(verbose_name="Продолжительность проклятья")
    likes = models.IntegerField(default=0, verbose_name="Лайки")
    link = models.URLField(null=True, default=None, verbose_name="Ссылка на профиль")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Последнее изменение")

    is_active = models.BooleanField(default=True, verbose_name="Действующее проклятье")

    class Meta:
        verbose_name = 'Проклятье'
        verbose_name_plural = 'Проклятья'