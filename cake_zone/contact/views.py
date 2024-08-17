from django.shortcuts import render, redirect
from .models import Information_Contact
from .forms import MessageFromCustomerForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = MessageFromCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:index')

        context = {
            'message_form': form,
            'contacts': Information_Contact.objects.first()
        }
        return render(request, 'contact.html', context=context)
    else:
        context = {
            'message_form': MessageFromCustomerForm(),
            'contacts': Information_Contact.objects.first()
        }
        return render(request, 'contact.html', context=context)