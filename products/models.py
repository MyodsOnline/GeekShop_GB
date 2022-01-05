from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['pk']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название товара')
    description = models.TextField(blank=True, verbose_name='Описание товара')
    short_description = models.CharField(max_length=60, verbose_name='Краткое описание')
    image = models.ImageField(upload_to='products_images', blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='Цена товара')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество товара')
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-updated_at']

    def __str__(self):
        return self.name
