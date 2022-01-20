import random
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.template.loader import render_to_string

from basketapp.models import Basket
from products.models import Product


@login_required
def basket(request):
    title = f'Корзина {request.user.username}'
    basket_items = Basket.objects.filter(user=request.user).order_by('product__category')
    sample_list = random.sample([x for x in range(1, len(Product.objects.all())+1)], 4)
    sample_products = []
    for i in sample_list:
        sample_products.append(Product.objects.get(pk=i))
    context = {
        'title': title,
        'basket_items': basket_items,
        'sample_products': sample_products,
    }
    return render(request, 'basketapp/basket.html', context)


@login_required
def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('products:detail', args=[pk]))

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, pk, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        new_basket_item = Basket.objects.get(pk=int(pk))

        if quantity > 0:
            new_basket_item.quantity = quantity
            new_basket_item.save()
        else:
            new_basket_item.delete()

        basket_items = Basket.objects.filter(user=request.user).order_by('product__category')

        context = {
            'basket_items': basket_items,
        }
        result = render_to_string('basketapp/includes/inc_basket.html', context)

        return JsonResponse({'result': result})
