from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse

from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm


def login(request):
    title = 'Вход'
    login_form = ShopUserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('mainapp:home'))

    context = {
        'title': title,
        'greeting': 'Вход',
        'login_form': login_form,
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('mainapp:home'))


def register(request):
    title = 'Регистрация'

    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Вы успешно зарегистрированы!')
            return HttpResponseRedirect(reverse('auth:login'))

    else:
        register_form = ShopUserRegisterForm()

    context = {
        'title': title,
        'greeting': 'Регистрация',
        'register_form': register_form,
    }

    return render(request, 'authapp/register.html', context)


def edit(request):
    title = 'Редактирование'

    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, 'Данные успешно обновлены!')
            return HttpResponseRedirect(reverse('auth:edit'))
        else:
            print(edit_form.errors)
    else:
        edit_form = ShopUserEditForm(instance=request.user)

    content = {'title': title,
               'greeting': 'Редактирование',
               'edit_form': edit_form,
               }

    return render(request, 'authapp/edit.html', content)
