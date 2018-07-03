from django.shortcuts import render
from django.http import HttpResponse
from .models import Repair

# Create your views here.

def get_repair(request):
    repair = Repair.objects.all()
    return render(request, "repair/repair.html", {'repair': repair})