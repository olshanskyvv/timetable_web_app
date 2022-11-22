from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class MyUserAdmin(UserAdmin):
    list_display = ('username', 'last_name', 'first_name', 'group', 'email', 'is_elder')
    list_display_links = ('username', 'last_name', 'first_name')
    search_fields = ('username', 'last_name', 'first_name')
    list_editable = ('is_elder',)


admin.site.register(User, MyUserAdmin)
