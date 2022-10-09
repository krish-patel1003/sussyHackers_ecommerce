from django.shortcuts import render

from .models import *
# Create your views here.

def home(request):
    content = {"name" : "Krish"}
    return render(request, 'backend/base.html', context=content)

