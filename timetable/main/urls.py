from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('timetable', views.timetable, name='timetable'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
]