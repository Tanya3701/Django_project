from .models import Category, Product


def product_list_by_category_context_processor(request):
    products = Product.objects.all()
    context = {"products": products}
    return context


def category_list_context_processor(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return context
