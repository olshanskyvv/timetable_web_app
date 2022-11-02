from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('timetable', views.TimetableView.as_view(), name='timetable'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('profile/edit', views.UpdateUserView.as_view(), name='profile_edit'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.RegisterView.as_view(), name='register'),
]