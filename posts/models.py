from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    content = models.TextField(blank=True)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
