from django.contrib import admin

from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("header", "content")
    list_filter = ("header",)
    search_fields = ("header",)
