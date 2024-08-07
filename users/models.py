from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    name = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=30, verbose_name='Телефон', **NULLABLE)
    city = models.CharField(max_length=30, verbose_name='Город', **NULLABLE)
    image = models.ImageField(upload_to='user', verbose_name='Изображение', **NULLABLE)
    tg_chat_id = models.CharField(max_length=35, verbose_name='id чата телеграмма')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
