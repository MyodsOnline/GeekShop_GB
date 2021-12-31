from django.shortcuts import render

from products.models import Product
from basketapp.models import Basket


def home(request):
    title = 'GeekShop'
    products_list = Product.objects.all()[:4]
    promo = [
        {'promo_title': 'Тенденции', 'promo_text': 'Опыт профессионалов', 'promo_slogan': 'Новое качество жизни'},
        {'promo_title': 'Решительность', 'promo_text': 'Скорее в отрыв!', 'promo_slogan': 'Мировые тенденции'},
        {'promo_title': 'Образ', 'promo_text': 'Следующий уровень комфорта', 'promo_slogan': 'Советы экспертов'},
    ]

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    context = {
        'title': title,
        'products_list': products_list,
        'promo': promo,
        'basket': basket,
    }
    return render(request, 'mainapp/index.html', context)


def contacts(request):
    title = 'Contacts'
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    context = {
        'title': title,
        'basket': basket,
    }
    return render(request, 'mainapp/contact.html', context)
