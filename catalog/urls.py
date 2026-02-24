from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig

from .views import base, contacts, home, product_info

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("product_info/<int:pk>/", product_info, name="product_info"),
    path("base/", base, name="base"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
