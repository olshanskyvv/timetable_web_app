from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from .code.searcher import find_group_url
from .code.parser import parse
from .utils import DataMixin
from .forms import *


class IndexView(DataMixin, TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))


class TimetableView(LoginRequiredMixin, DataMixin, TemplateView):
    template_name = 'main/timetable.html'
    login_url = reverse_lazy('login')

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


class RegisterView(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))
