from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms
from re import match

from django.forms import ModelForm

from .models import *


def group_is_valid(value):
    if not match(r'\w{3}-\d{3}', value):
        raise forms.ValidationError("Группа не соответствует формату: AAA-111")


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': 'form-input'}), required=False)
    group = forms.CharField(label='Номер группы', validators=[group_is_valid], widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'group', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class UpdateUserForm(ModelForm):
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    group = forms.CharField(label='Номер группы', validators=[group_is_valid], widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'group']


class NoteUpdateForm(ModelForm):
    note = forms.CharField(label='Заметки', required=False, widget=forms.Textarea(attrs={'class': 'form-input'}))

    class Meta:
        model = Lesson
        fields = ['note']
