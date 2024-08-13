from .views import index
from django.urls import path

app_name = 'menu'

urlpatterns = [
    path('', index,name = 'index'),
]
