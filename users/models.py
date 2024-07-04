from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True, verbose_name='Еmail')
    phone = models.CharField(max_length=35, verbose_name='Телефон', blank=True, null=True)
    avatar = models.ImageField(upload_to='users/avatars/', verbose_name='Аватар', blank=True, null=True)
    token = models.CharField(max_length=100, verbose_name='Токен', blank=True, null=True)
    is_email_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        permissions = [
            ('deactivate_user', 'Can deactivate user'),
            ('view_all_users', 'Can view all users'),
        ]

    def __str__(self):
        return self.email
