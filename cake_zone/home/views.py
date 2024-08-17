from django.shortcuts import render
from .models import Review_Clients


def index(request):
    client = Review_Clients.objects.filter(is_visible=True)
    context = {
        'client':client,
    }
    return render(request,'home.html' , context=context)
