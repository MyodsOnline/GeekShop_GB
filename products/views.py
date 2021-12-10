from django.shortcuts import render
import os
import json

SOURCE_DIR = os.path.dirname(__file__)
source_file = os.path.join(SOURCE_DIR, 'static/products.json')


def products(request):
    title = 'Products'
    links_menu = [
        {'href': 'products', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    products_json = json.load(open(source_file, encoding='utf-8'))
    context = {
        'title': title,
        'links_menu': links_menu,
        'products_json': products_json,
    }
    return render(request, 'products/products.html', context)
