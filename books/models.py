from django.db import models
from django.contrib.auth.models import User


# Create your models here this creates a table for eg:books
class Book(models.Model):
    name = models.CharField(max_length=254, blank=False)
    author = models.CharField(max_length=254, blank=False)
    isbn = models.CharField(max_length=254, blank=False)
    notes = models.TextField(blank=False)
    image = models.ImageField(upload_to='images', default="images/default.png")
    owner = models.ForeignKey(User, related_name='books', null=False)
    def __str__(self):
        return self.name