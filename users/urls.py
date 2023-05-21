from django.urls import path
from . import views # in current directory import views.py file

urlpatterns = [
    path('', views.register, name='register'), #an empty path redirect to users-register
]