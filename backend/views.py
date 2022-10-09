from multiprocessing import context
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .models import *
from .forms import UserRegistrationForm
from .filters import ProductFilter
# Create your views here.

def home(request):
    content = {"name" : "Krish"}
    return render(request, 'backend/base.html', context=content)

class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'backend/user_create.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    success_message = "Your profile was created successfully"

def category(request):

    data = Category.objects.all()

    print(data)

    return render(request, 'backend/demo.html', {"data": data})

def products(request):

    data = Product.objects.all()
    filter_data = ProductFilter(request.GET, queryset=data)
    print(filter_data.qs)

    return render(request, 'backend/demo.html', {"filter_data": filter_data})