from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    first_name = forms.CharField(max_length=100, label = "First Name")
    last_name = forms.CharField(max_length=100, label = "Last Name")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')
        