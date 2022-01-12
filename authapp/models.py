from datetime import timedelta

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatar', blank=True)
    age = models.BooleanField(verbose_name='Возраст', default=False)
    birth_date = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    promo_accept = models.BooleanField(default=True, verbose_name='Промоакции')

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)))

    def is_activation_key_expires(self):
        if now() <= self.activation_key_expires:
            return False
        else:
            return True

    def __str__(self):
        return self.username
