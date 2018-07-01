from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def get_contact(request):
    return render(request, "contact/contact.html")