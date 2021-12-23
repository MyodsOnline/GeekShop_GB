from django.shortcuts import render

from products.models import Product
from basketapp.models import Basket


def home(request):
    title = 'GeekShop'
    products_list = Product.objects.all()[:4]
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    context = {
        'title': title,
        'products_list': products_list,
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
