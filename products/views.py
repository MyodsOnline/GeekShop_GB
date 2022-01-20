import random
from django.shortcuts import render, get_object_or_404
import os
import json

from basketapp.models import Basket
from products.models import ProductCategory, Product

SOURCE_DIR = os.path.dirname(__file__)
source_file = os.path.join(SOURCE_DIR, 'static/products.json')


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)
    if same_products:
        return same_products
    else:
        same_products = Product.objects.all().order_by('price')[:4]
        return same_products


def products(request, pk=None):
    title = 'Products'
    links_menu = ProductCategory.objects.filter(is_active=True)
    products_json = json.load(open(source_file, encoding='utf-8'))
    basket = get_basket(request.user)
    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    products_list = Product.objects.all().order_by('price')

    if pk is not None:
        category = get_object_or_404(ProductCategory, pk=pk)
        products_in_category = Product.objects.filter(category__pk=pk).order_by('price')

        context = {
            'title': title,
            'links_menu': links_menu,
            'products': products_in_category,
            'category': category,
            'basket': basket,
            'same_products': same_products,
            'hot_product': hot_product
        }
        return render(request, 'products/products.html', context)

    context = {
        'title': title,
        'links_menu': links_menu,
        'products_list': products_list,
        'basket': basket,
        'same_products': same_products,
        'hot_product': hot_product
    }
    return render(request, 'products/products.html', context)


def product(request, pk):
    title = Product.objects.get(pk=pk).name
    context = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
    }
    return render(request, 'products/product_detail.html', context)
