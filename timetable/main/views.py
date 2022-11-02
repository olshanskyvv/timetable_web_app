from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView

from .code.searcher import find_group_url
from .code.parser import parse
from .utils import DataMixin
from .forms import *
from .code.exceptions import *


class IndexView(DataMixin, TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))


class AboutView(DataMixin, TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='О нас')
        return dict(list(context.items()) + list(c_def.items()))


class TimetableView(LoginRequiredMixin, DataMixin, TemplateView):
    template_name = 'main/timetable.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        error_type = None
        error_text = None
        table = None
        try:
            table_url = find_group_url(self.request.user.group)
            table = parse(table_url)
        except ConnectionError as c:
            print(c)
            error_type = 'ConnectionFault'
            error_text = str(c)
        except GroupNotFound as nf:
            print(nf)
            error_type = 'GroupNotFound'
            error_text = str(nf)
        except Exception as e:
            print(e)
            error_type = 'error'
            error_text = str(e)

        c_def = self.get_user_context(title='Расписание', table=table, error_type=error_type, error_text=error_text)
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('timetable')


def logout_user(request):
    logout(request)
    return redirect('login')


class RegisterView(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('timetable')


class ProfileView(LoginRequiredMixin, DataMixin, TemplateView):
    template_name = 'main/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        profile = [
            {'title': 'Имя', 'field': user.first_name, },
            {'title': 'Фамилия', 'field': user.last_name},
            {'title': 'Email', 'field': user.email},
            {'title': 'Номер группы', 'field': user.group},
        ]
        c_def = self.get_user_context(title='Профиль', profile=profile)
        return dict(list(context.items()) + list(c_def.items()))


class UpdateUserView(LoginRequiredMixin, DataMixin, UpdateView):
    form_class = UpdateUserForm
    context_object_name = 'user'
    model = User
    template_name = 'main/profile_edit.html'
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.request.user
        c_def = self.get_user_context(title='Редактирование', profile=profile)
        return dict(list(context.items()) + list(c_def.items()))

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        form.save()
        return redirect(reverse_lazy('profile'))
