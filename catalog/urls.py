from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig

from .views import (ContactsView, ProductCreateView, ProductDeleteView,
                    ProductDetailView, ProductListByCategoryView,
                    ProductListView, ProductUpdateView)

app_name = CatalogConfig.name

urlpatterns = [
    path("product_list/", ProductListView.as_view(), name="product_list"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path(
        "product_detail/<int:pk>/",
        cache_page(60)(ProductDetailView.as_view()),
        name="product_detail",
    ),
    path("create/", ProductCreateView.as_view(), name="product_create"),
    path("<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path(
        "product_by_categories/<int:category_id>/",
        ProductListByCategoryView.as_view(),
        name="product_by_categories",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
