from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatar', blank=True)
    age = models.BooleanField(verbose_name='Возраст', default=False)
    birth_date = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    promo_accept = models.BooleanField(default=True, verbose_name='Промоакции')

    def __str__(self):
        return self.username
