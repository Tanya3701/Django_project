from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'password')
    list_filter = ('username', 'email')
    ordering = ('username',)
