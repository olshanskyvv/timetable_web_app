from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    return HttpResponse('<h1>Страница с входом</h1>')


def register(request):
    return HttpResponse('<h1>Страница с регистрацией</h1>')
