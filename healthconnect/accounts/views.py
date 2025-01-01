from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView
from django.http import HttpResponse

from .forms import SignUpForm

# Create your views here.

class SignUpView(CreateView):
    
    form_class = SignUpForm
    template_name ='signup.html'
    success_url = reverse_lazy('home')

def loginview(request):
    return HttpResponse('Login here')

def homeview(request):
    return HttpResponse('Home page')