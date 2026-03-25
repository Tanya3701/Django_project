from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from blogs.models import Blog


class BlogListView(ListView):
    """Класс представления для списка блогов"""
    model = Blog

    def get_queryset(self):
        queryset = Blog.objects.filter(published=True)
        return queryset


class BlogDetailView(DetailView):
    """Класс представления для деталей блогов"""
    model = Blog

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.view_count += 1
        obj.save()
        return obj


class BlogCreateView(CreateView):
    """Класс представления для создания блогов"""
    model = Blog
    fields = ("header", "content", "preview" "published")
    success_url = reverse_lazy("blogs:blog_list")


class BlogUpdateView(UpdateView):
    """Класс представления для редактирования блогов"""
    model = Blog
    fields = ("header", "content", "preview", "published")

    def get_success_url(self):
        return reverse_lazy("blogs:blog_detail", kwargs={"pk": self.object.pk})


class BlogDeleteView(DeleteView):
    """Класс представления для удаления блогов"""
    model = Blog
    success_url = reverse_lazy("blogs:blog_list")
