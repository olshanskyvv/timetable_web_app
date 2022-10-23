from django.shortcuts import render
from django.http import HttpResponse

from .code.searcher import find_group_url
from .code.parser import parse


def index(request):
    return HttpResponse('<h1>Стартовая страница</h1>')


def timetable(request):
    table = parse(find_group_url('УИС-212'))
    return render(request, 'main/timetable.html', {'table': table})


def login(request):
    return HttpResponse('<h1>Страница с входом</h1>')


def register(request):
    return HttpResponse('<h1>Страница с регистрацией</h1>')
