from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    
    email = forms.EmailField(label = "Email")
    first_name = forms.CharField(max_length=100, label = "First Name")
    last_name = forms.CharField(max_length=100, label = "Last Name")
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, label = "Role")

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('first_name', 'last_name', 'email','role' , 'username', 'password1', 'password2')
        

class UserUpdateForm(UserChangeForm):
    # Inherits from the built-in UserChangeForm's Meta 
    # for modify user details in the admin panel
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        field = UserCreationForm.Meta.fields
    
 


class CustomAuthenticationForm(AuthenticationForm):
    
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email and password:
            self.user_cache = authenticate(
                self.request,
                username=email,  # authenticate expects username parameter
                password=password
            )
            if self.user_cache is None:
                raise forms.ValidationError('Invalid email or password')
        return self.cleaned_data   