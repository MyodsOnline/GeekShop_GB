from django.conf import settings
from django.db import models

from products.models import Product


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=0)

    add_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
