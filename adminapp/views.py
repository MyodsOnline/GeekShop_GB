from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from adminapp.forms import ShopUserAdminEditForm, ProductEditForm, ProductCategoryEditForm, UserAdminUpdateForm
from authapp.forms import ShopUserEditForm, ShopUserRegisterForm

from authapp.models import ShopUser
from products.models import Product, ProductCategory


# @user_passes_test(lambda u: u.is_superuser)
# def users(request):
#     title = 'админка/пользователи'
#     users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
#     context = {
#         'title': title,
#         'objects': users_list
#     }
#     return render(request, 'adminapp/users.html', context)


class UserListView(ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'админка/пользователи'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def user_create(request):
#     title = 'пользователи/cоздание'
#     if request.method == 'POST':
#         user_form = ShopUserRegisterForm(request.POST, request.FILES)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:users'))
#     else:
#         user_form = ShopUserRegisterForm()
#     context = {
#         'title': title,
#         'user_form': user_form,
#     }
#     return render(request, 'adminapp/user_update.html', context)


class UserCreateView(CreateView):
    model = ShopUser
    template_name = 'adminapp/user_create.html'
    form_class = ShopUserRegisterForm
    success_url = reverse_lazy('admin_staff:users')


# @user_passes_test(lambda u: u.is_superuser)
# def user_update(request, pk):
#     title = 'пользователи/редактирование'
#     edit_user = get_object_or_404(ShopUser, pk=pk)
#     if request.method == 'POST':
#         edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:users'))
#     else:
#         edit_form = ShopUserAdminEditForm(instance=edit_user)
#     context = {
#         'title': title,
#         'user_form': edit_form,
#     }
#     return render(request, 'adminapp/user_update.html', context)


class UserUpdateView(UpdateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('admin_staff:users')
    form_class = UserAdminUpdateForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'пользователи/редактирование'
        return context


# @user_passes_test(lambda u: u.is_superuser)
# def user_delete(request, pk):
#     title = 'пользователи/удаление'
#     user = get_object_or_404(ShopUser, pk=pk)
#     if request.method == 'POST':
#         user.is_active = False
#         user.save()
#         return HttpResponseRedirect(reverse('admin_staff:users'))
#     context = {
#         'title': title,
#         'user_to_delete': user,
#     }
#     return render(request, 'adminapp/user_delete.html', context)


class UserDeleteView(DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_delete.html'
    success_url = reverse_lazy('admin_staff:users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    title = 'админка/категории'
    categories_list = ProductCategory.objects.all()
    context = {
        'title': title,
        'objects': categories_list
    }
    return render(request, 'adminapp/categories.html', context)


@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    title = 'категории/cоздание'
    if request.method == 'POST':
        category_form = ProductCategoryEditForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('admin_staff:categories'))
    else:
        category_form = ProductCategoryEditForm()
    context = {
        'title': title,
        'category_form': category_form,
    }
    return render(request, 'adminapp/categories_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def category_update(request, pk):
    title = 'категории/редактирование'
    edit_category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        edit_form = ProductCategoryEditForm(request.POST, request.FILES, instance=edit_category)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin_staff:categories'))

    else:
        edit_form = ProductCategoryEditForm(instance=edit_category)
    context = {
        'title': title,
        'category_form': edit_form,
    }

    return render(request, 'adminapp/categories_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, pk):
    title = 'категории/cоздание'
    category_to_delete = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        category_to_delete.is_active = False
        category_to_delete.save()
        return HttpResponseRedirect(reverse('admin_staff:categories'))
    context = {
        'title': title,
        'category_to_delete': category_to_delete,
    }
    return render(request, 'adminapp/category_delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def products_list(request, page=1):
    title = 'админка/товары'
    context = {'title': title}
    products_list = Product.objects.all().order_by('name')

    paginator = Paginator(products_list, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context['objects'] = products_paginator

    return render(request, 'adminapp/products_read.html', context)




@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    title = 'админка/продукт'
    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')
    context = {
        'title': title,
        'category': category,
        'objects': products_list,
    }
    return render(request, 'adminapp/products.html', context)


@user_passes_test(lambda u: u.is_superuser)
def product_create(request, pk):
    title = 'продукт/cоздание'
    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('admin_staff:products', args=[pk]))
    else:
        product_form = ProductEditForm(initial={'category': category})
    context = {
        'title': title,
        'update_form': product_form,
    }
    return render(request, 'adminapp/product_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def product_read(request, pk):
    title = 'продукт/подробнее'
    product = get_object_or_404(Product, pk=pk)
    context = {
        'title': title,
        'object': product,
    }
    return render(request, 'adminapp/product_read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    title = 'продукт/редактирование'
    edit_product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin_staff:product_read', args=[edit_product.pk]))
    else:
        edit_form = ProductEditForm(instance=edit_product)
    context = {
        'title': title,
        'update_form': edit_form,
        'category': edit_product.category
    }
    return render(request, 'adminapp/product_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, pk):
    title = 'продукт/удаление'
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.is_active = False
        product.save()
        return HttpResponseRedirect(reverse('admin_staff:products', args=[product.category.pk]))
    context = {
        'title': title,
        'product_to_delete': product,
    }
    return render(request, 'adminapp/product_delete.html', context)
