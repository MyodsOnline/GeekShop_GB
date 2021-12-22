import random
from django.shortcuts import render, get_object_or_404
import os
import json

from products.models import ProductCategory, Product

SOURCE_DIR = os.path.dirname(__file__)
source_file = os.path.join(SOURCE_DIR, 'static/products.json')


def products(request, pk=None):
    title = 'Products'
    links_menu = ProductCategory.objects.all()
    products_json = json.load(open(source_file, encoding='utf-8'))
    same_products = Product.objects.all()

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

            same_list = random.sample([x for x in range(1, len(Product.objects.all())+1)], 3)
            same_products = []
            for i in same_list:
                same_products.append(Product.objects.get(pk=i))

        context = {
            'title': title,
            'links_menu': links_menu,
            'products_json': products_json,
            'products': products,
            'category': category,
            'same_products': same_products,
        }
        return render(request, 'products/products.html', context)

    context = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
    }
    return render(request, 'products/products.html', context)
