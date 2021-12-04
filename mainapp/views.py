from django.shortcuts import render


def home(request):
    return render(request, 'mainapp/index.html')


def contacts(request):
    return render(request, 'mainapp/contact.html')
