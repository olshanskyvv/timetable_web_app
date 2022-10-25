from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from .code.searcher import find_group_url
from .code.parser import parse


# def index(request):
#     return render(request, 'main/index.html')


class IndexView(TemplateView):
    template_name = 'main/index.html'


class TimetableView(TemplateView):
    template_name = 'main/timetable.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table'] = parse(find_group_url('УИС-212'))
        return context


class LoginView(TemplateView):
    template_name = 'main/login.html'


class RegisterView(TemplateView):
    template_name = 'main/register.html'
