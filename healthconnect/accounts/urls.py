from django.urls import path

from .views import homeview, SignUpView, CustomloginView

urlpatterns = [
    path('login/', CustomloginView.as_view(), name='login'),
    path('home/',homeview.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
       
]
