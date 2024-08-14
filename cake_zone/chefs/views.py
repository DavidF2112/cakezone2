from django.shortcuts import render
from .models import Chefs_Information

def index(request):
    staff = Chefs_Information.objects.filter(is_visible=True).order_by('sort')
    context = {
        'staff': staff
    }

    return render(request,'chefs.html' , context=context)
