from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from products.models import Product
from basketapp.models import Basket
from mainapp.models import Promo


def home(request, page=1):
    title = 'GeekShop'
    promo = Promo.objects.all()

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': title,
        'promo': promo,
        'basket': basket,
    }

    products_list = Product.objects.all()[1:4] if request.resolver_match.url_name == 'new' else Product.objects.all()

    paginator = Paginator(products_list, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context['products_list'] = products_paginator

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
