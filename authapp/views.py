from django.core.mail import send_mail
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from django.db import transaction

from Geekshop import settings
from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm, ShopUserProfileEditForm
from authapp.models import ShopUser


def login(request):
    title = 'Вход'
    login_form = ShopUserLoginForm(data=request.POST or None)

    next = request.GET['next'] if 'next'  in request.GET.keys() else ''

    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse('mainapp:home'))

    context = {
        'title': title,
        'login_form': login_form,
        'next': next,
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
            user = register_form.save()
            if send_verify_mail(user):
                print('Сообщение отправлено')
                messages.success(request, 'Вы успешно зарегистрированы!')
                return HttpResponseRedirect(reverse('auth:login'))
            else:
                print('Сообщение отправлено')
                messages.error(request, 'ERROR')
                return HttpResponseRedirect(reverse('auth:login'))

    else:
        register_form = ShopUserRegisterForm()

    context = {
        'title': title,
        'greeting': 'Регистрация',
        'register_form': register_form,
    }

    return render(request, 'authapp/register.html', context)


@transaction.atomic
def edit(request):
    title = 'Редактирование'

    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        profile_form = ShopUserProfileEditForm(request.POST, instance=request.user.shopuserprofile)
        if edit_form.is_valid() and profile_form.is_valid():
            edit_form.save()
            messages.success(request, 'Данные успешно обновлены!')
            return HttpResponseRedirect(reverse('auth:edit'))
        else:
            print(edit_form.errors)
    else:
        edit_form = ShopUserEditForm(instance=request.user)
        profile_form = ShopUserProfileEditForm(instance=request.user.shopuserprofile)

    context = {'title': title,
               'greeting': 'Редактирование',
               'edit_form': edit_form,
               'profile_form': profile_form,
               }

    return render(request, 'authapp/edit.html', context)


def send_verify_mail(user):
    verify_link = reverse('auth:verify', args=[user.email, user.activation_key])
    title = f'Подтверждение учетной записи {user.username}'
    message = f'Для активации учетной записи {user.username} перейдите по ссылке {settings.DOMAIN_NAME}{verify_link}'

    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def verify(request, email, activation_key):
    try:
        user = ShopUser.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expires():
            user.is_active = True
            user.save()
            auth.login(request, user)
            return render(request, 'authapp/verification.html')
        else:
            print(f'Error activation user: {user}')
            return render(request, 'authapp/verification.html')
    except Exception as err:
        print(f'Error activation user: {err.args}')
        return HttpResponseRedirect(reverse('mainapp:home'))
