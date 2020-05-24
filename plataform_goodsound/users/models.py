from django.db import models

# Create your models here.
class Users(models.Model):
    avatar = models.FileField(upload_to="media/%Y/%m/%d/")
    name = models.CharField(max_length=200,verbose_name='Username')
    email = models.EmailField()
    age = models.IntegerField()
    date_entry_plataform = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name', 'email', 'date_entry_plataform']
        verbose_name = "User"
        verbose_name_plural = "Users"