from django.db import models


class Promo(models.Model):
    promo_title = models.CharField(max_length=100, unique=True, verbose_name='promo_title')
    promo_text = models.CharField(max_length=100, unique=True, verbose_name='promo_text')
    promo_slogan = models.CharField(max_length=100, unique=True, verbose_name='promo_slogan')

    def __str__(self):
        return self.promo_title
