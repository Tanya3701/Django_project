from django.contrib import admin

from .models import Category, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product_name",
        "price",
        "category",
        "description",
        "created_at",
        "updated_at",
        "published",
    )
    list_filter = ("id",)
    search_fields = ("product_name", "description")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category_name", "description")
    list_filter = ("category_name",)
    search_fields = ("category_name", "description")
