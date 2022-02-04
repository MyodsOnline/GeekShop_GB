import random
from django.shortcuts import render, get_object_or_404
import os
import json
from django.conf import settings
from django.core.cache import cache

from products.models import ProductCategory, Product

SOURCE_DIR = os.path.dirname(__file__)
source_file = os.path.join(SOURCE_DIR, 'static/products.json')


def get_links_menu():
    if settings.LOW_CACHE:
        key = 'links_menu'
        links_menu = cache.get(key)
        if links_menu is None:
            links_menu = ProductCategory.objects.filter(is_active=True)
            cache.set(key, links_menu)
        return links_menu
    else:
        return ProductCategory.objects.filter(is_active=True)


def get_category(pk):
    if settings.LOW_CACHE:
        key = f'category_{pk}'
        category = cache.get(key)
        if category is None:
            category = get_object_or_404(ProductCategory, pk=pk)
            cache.set(key, category)
        return category
    else:
        return get_object_or_404(ProductCategory, pk=pk)


def get_products():
    if settings.LOW_CACHE:
        key = 'products'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(is_active=True)
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(is_active=True)


def get_product(pk):
    if settings.LOW_CACHE:
        key = 'products'
        product = cache.get(key)
        if product is None:
            product = get_object_or_404(Product, pk=pk)
            cache.set(key, product)
        return product
    else:
        return get_object_or_404(Product, pk=pk)


def get_products_ordered_by_price():
    if settings.LOW_CACHE:
        key = 'products_ordered_by_price'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(is_active=True, category__is_active=True).order_by('price')


def get_products_in_category_ordered_by_price(pk):
    if settings.LOW_CACHE:
        key = f'products_in_category_ordered_by_price_{pk}'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(category__pk=pk, category__is_active=True).order_by('price')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(category__pk=pk, category__is_active=True).order_by('price')


def get_hot_product():
    products = get_products()
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
    links_menu = get_links_menu()
    products_json = json.load(open(source_file, encoding='utf-8'))
    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    products_list = get_products_ordered_by_price()

    if pk is not None:
        category = get_object_or_404(ProductCategory, pk=pk)
        products_in_category = get_products_in_category_ordered_by_price(pk)

        context = {
            'title': title,
            'links_menu': links_menu,
            'products': products_in_category,
            'category': category,
            'same_products': same_products,
            'hot_product': hot_product
        }
        return render(request, 'products/products.html', context)

    context = {
        'title': title,
        'links_menu': links_menu,
        'products_list': products_list,
        'same_products': same_products,
        'hot_product': hot_product
    }
    return render(request, 'products/products.html', context)


def product(request, pk):
    title = Product.objects.get(pk=pk).name
    context = {
        'title': title,
        'links_menu': get_links_menu(),
        'product': get_product(pk),
    }
    return render(request, 'products/product_detail.html', context)
