from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .forms import  SignUpForm, UserUpdateForm

from django.contrib.auth.models import User

class CustomUserAdmin(UserAdmin):
    #create a new user
    add_form = SignUpForm
    # edit a user
    form = UserUpdateForm
    model = User
    list_display = ('username', 'email', 'is_staff', 'is_superuser','first_name','last_name')
    
# admin.site.register(User, CustomUserAdmin)