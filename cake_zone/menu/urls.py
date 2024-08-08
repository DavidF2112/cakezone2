from .views import menu
from django.urls import path

name = 'menu'

urlpatterns = [
    path('', menu,name = 'menu'),
]
