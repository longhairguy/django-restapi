from django.db import models

# Create your models here.

class Todo(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    title = models.CharField(max_length=40)
    story = models.TextField()

    class Meta:
        ordering = ('created_at',)
