from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    """Команда для наполнения базы данных"""

    help = "Add test products to the database"

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()
        category, _ = Category.objects.get_or_create(
            category_name="Стулья", description="Разные стулья"
        )

        products = [
            {
                "product_name": "Деревянный",
                "description": "Деревянный стул",
                "image": "wooden.jpg",
                "category": category,
                "price": 1000,
            },
            {
                "product_name": "Электрический",
                "description": "Электрический стул",
                "image": "electric.jpg",
                "category": category,
                "price": 1200,
            },
        ]

        for item in products:
            product, created = Product.objects.get_or_create(**item)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully added product: {product.product_name}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Product already exists: {product.product_name}"
                    )
                )
