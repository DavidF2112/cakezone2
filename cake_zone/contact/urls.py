from .views import contact
from django.urls import path

name = 'contact'

urlpatterns = [
    path('', contact,name = 'contact'),
]
