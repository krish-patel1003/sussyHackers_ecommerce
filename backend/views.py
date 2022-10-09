from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .models import *
from .forms import UserRegistrationForm
# Create your views here.

def home(request):
    content = {"name" : "Krish"}
    return render(request, 'backend/base.html', context=content)

class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'backend/user_create.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    success_message = "Your profile was created successfully"