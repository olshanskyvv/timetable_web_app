from django.shortcuts import render

from .code.searcher import find_group_url
from .code.parser import parse


def index(request):
    return render(request, 'main/index.html')


def timetable(request):
    table = parse(find_group_url('УИС-212'))
    return render(request, 'main/timetable.html', {'table': table})


def login(request):
    return render(request, 'main/login.html')


def register(request):
    return render(request, 'main/register.html')
