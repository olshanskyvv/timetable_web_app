from django.shortcuts import render
from django.http import HttpResponse


def timetable(request):
    return HttpResponse('<h1>Страница с расписанием</h1>')
