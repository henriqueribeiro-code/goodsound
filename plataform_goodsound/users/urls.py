from django.urls import path
from .views import *

urlpatterns = [
 path('add/', add, name='add_user'),
]
