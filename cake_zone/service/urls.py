from .views import index
from django.urls import path

app_name = 'service'

urlpatterns = [
    path('', index,name = 'index'),
]
