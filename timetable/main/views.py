from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from .code.searcher import find_group_url
from .code.parser import parse
from .utils import DataMixin


class IndexView(DataMixin, TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))


class TimetableView(DataMixin, TemplateView):
    template_name = 'main/timetable.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        table = parse(find_group_url('УИС-212'))
        c_def = self.get_user_context(title='Расписание',
                                      table=table)
        return dict(list(context.items()) + list(c_def.items()))


class LoginView(DataMixin, TemplateView):
    template_name = 'main/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Вход')
        return dict(list(context.items()) + list(c_def.items()))


class RegisterView(DataMixin, TemplateView):
    template_name = 'main/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))
