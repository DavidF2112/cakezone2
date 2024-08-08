from .views import chefs
from django.urls import path

name = 'chefs'

urlpatterns = [
    path('', chefs,name = 'chefs'),
]
