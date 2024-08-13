from django.shortcuts import render
from .models import Category


def index(request):
    categories = Category.objects.filter(is_visible=True)
    context = {
        'categories':categories,
    }
    return render(request,'menu.html' , context=context)
