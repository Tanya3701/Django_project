from django.db import models

from users.models import User


class Category(models.Model):
    """Класс категории"""

    category_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.category_name

    class Meta:
        """Способ отображения"""

        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["category_name"]


class Product(models.Model):
    """Класс продукты"""

    product_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(verbose_name="Фото товара", null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    owner = models.ForeignKey(
        User, verbose_name="Владелец", on_delete=models.SET_NULL, blank=True, null=True
    )
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name

    class Meta:
        """Способ отображения"""

        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["product_name"]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]
