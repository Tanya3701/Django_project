from django.db import models


class Blog(models.Model):
    header = models.CharField(max_length=100)
    content = models.TextField()
    preview = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        ordering = ["header"]
