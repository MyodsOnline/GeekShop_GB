# Generated by Django 3.2.9 on 2021-12-17 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-updated_at'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'ordering': ['pk'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
    ]
