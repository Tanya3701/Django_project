from django.db import models


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
    image = models.ImageField(
        verbose_name="Фото товара", null=True
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.product_name

    class Meta:
        """Способ отображения"""

        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["product_name"]
