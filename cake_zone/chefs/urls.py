from .views import index
from django.urls import path

app_name = 'chefs'

urlpatterns = [
    path('', index,name = 'index'),
]
