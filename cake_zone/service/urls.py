from .views import service
from django.urls import path

name = 'service'

urlpatterns = [
    path('', service,name = 'service'),
]
