from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


class ProductService:

    @staticmethod
    def get_products_cache():
        """Получает данные о товаре из кэша или БД"""
        if not CACHE_ENABLED:
            return Product.objects.all()
        key = "products"
        products = cache.get(key)
        if products is not None:
            return products
        products = Product.objects.all()
        cache.set(key, products)
        return products

    @staticmethod
    def get_product_by_id(category_id):
        """Сортирует товар по категориям"""
        products = Product.objects.filter(category_id=category_id)
        if products is not None:
            return products
        return None
