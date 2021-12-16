from django.shortcuts import render

from products.models import Product


def home(request):
    title = 'GeekShop'
    products_list = Product.objects.all()[:4]
    context = {
        'title': title,
        'products_list': products_list,
    }
    return render(request, 'mainapp/index.html', context)


def contacts(request):
    title = 'Contacts'
    context = {
        'title': title
    }
    return render(request, 'mainapp/contact.html', context)
