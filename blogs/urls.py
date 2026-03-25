from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blogs.apps import BlogsConfig
from blogs.views import (BlogCreateView, BlogDeleteView, BlogDetailView,
                         BlogListView, BlogUpdateView)

app_name = BlogsConfig.name

urlpatterns = [
    path("blog_list/", BlogListView.as_view(), name="blog_list"),
    path("blog_detail/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("create/", BlogCreateView.as_view(), name="blog_create"),
    path("<int:pk>/update/", BlogUpdateView.as_view(), name="blog_update"),
    path("<int:pk>/delete/>", BlogDeleteView.as_view(), name="blog_delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
