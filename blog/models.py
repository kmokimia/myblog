from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    content = models.TextField(verbose_name="محتوا")
    author = models.CharField(max_length=100, verbose_name="نویسنده")
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name="تاریخ ایجاد")
    is_published = models.BooleanField(default=True, verbose_name="منتشر شده؟")

    def __str__(self):
        return self.title
