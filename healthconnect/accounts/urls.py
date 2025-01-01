from django.urls import path
from django.contrib.auth.views import LoginView

from .views import homeview, SignUpView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('home/',homeview, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
       
]
