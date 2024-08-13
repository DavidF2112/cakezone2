from .views import index
from django.urls import path

app_name = 'home'

urlpatterns = [
    path('', index,name = 'index'),
]
