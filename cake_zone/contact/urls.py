from .views import index
from django.urls import path

app_name = 'contact'

urlpatterns = [
    path('', index,name = 'index'),
]
