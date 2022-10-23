from django.shortcuts import render

from .code.searcher import find_group_url
from .code.parser import parse


def timetable(request):
    table = parse(find_group_url('УИС-212'))
    return render(request, 'main/timetable.html', {'table': table})
