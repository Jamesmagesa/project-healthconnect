from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView
from django.http import HttpResponse
from django.contrib.auth.views import LoginView

from .forms import SignUpForm, CustomAuthenticationForm

# Create your views here.
class CustomloginView(LoginView):
    
    AuthenticationForm_form = CustomAuthenticationForm
    
    template_name = 'login.html'  
    success_url = reverse_lazy('home')   

    def form_valid(self, form):
        """Override form_valid to handle successful login"""
        super().form_valid(form)
        # Call super().form_valid(form) which handles the redirection
        return redirect(self.get_success_url())

class SignUpView(CreateView):
    
    form_class = SignUpForm
    template_name ='signup.html'
    success_url = reverse_lazy('login')


def homeview(request):
    return HttpResponse('Home page')