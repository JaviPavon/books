from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator

class Book(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    author = models.CharField(max_length=100)

    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)])

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):

        return self.title