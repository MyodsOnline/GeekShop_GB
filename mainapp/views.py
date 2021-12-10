from django.shortcuts import render


def home(request):
    title = 'GeekShop'
    context = {
        'title': title
    }
    return render(request, 'mainapp/index.html', context)


def contacts(request):
    title = 'Contacts'
    context = {
        'title': title
    }
    return render(request, 'mainapp/contact.html', context)
