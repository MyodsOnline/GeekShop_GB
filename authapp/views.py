from django.shortcuts import render, HttpResponse


def test(request):
    return HttpResponse('<h1>Authapp</h1>')
