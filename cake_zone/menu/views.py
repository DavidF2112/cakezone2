from django.shortcuts import render
from .models import Category


def menu(request):
    categories = Category.objects.all()
    return f'{categories}'