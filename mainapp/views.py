from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from products.models import Product
from mainapp.models import Promo


def home(request, page=1):
    title = 'GeekShop'
    promo = Promo.objects.all()
    context = {
        'title': title,
        'promo': promo,
    }
    products_list = Product.objects.all().order_by(
        'updated_at') if request.resolver_match.url_name == 'new' else Product.objects.all()
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
    context = {
        'title': title,
    }
    return render(request, 'mainapp/contact.html', context)
