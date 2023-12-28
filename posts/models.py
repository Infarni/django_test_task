from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField(max_length=4096)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
