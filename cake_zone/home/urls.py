from .views import home
from django.urls import path

name = 'home'

urlpatterns = [
    path('', home,name = 'home'),
]
