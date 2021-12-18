from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from authapp.forms import ShopUserLoginForm


def test(request):
    return HttpResponse('<h1>Authapp</h1>')


def login(request):
    title = 'Вход'

    login_form = ShopUserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))

    context = {
        'title': title,
        'login_form': login_form,
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
