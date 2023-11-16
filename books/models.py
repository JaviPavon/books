from django.conf import settings
from django.db import models
from django.utils import timezone

class Book(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    author = models.CharField(max_length=10)

    rating = models.PositiveIntegerField

    created_at = models.DateTimeField(default=timezone.now)

    updated_at = models.DateTimeField(default=timezone.now)


    def __str__(self):

        return self.title