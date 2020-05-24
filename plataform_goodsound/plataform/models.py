from django.db import models
from singers.models import Singers
# Create your models here.


class Music(models.Model):
    name = models.CharField(max_length=200)
    duration = models.TimeField()
    singer = models.ForeignKey(Singers, on_delete=models.CASCADE)
    date_post = models.DateTimeField(auto_now_add=True)



