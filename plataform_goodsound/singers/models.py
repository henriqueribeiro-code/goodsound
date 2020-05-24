from django.db import models

# Create your models here.
class Singers(models.Model):
    name  = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)

