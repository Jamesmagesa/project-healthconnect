from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .forms import  SignUpForm, UserUpdateForm

from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    #create a new user
    add_form = SignUpForm
    # edit a user
    form = UserUpdateForm
    model = CustomUser
    list_display = ('username', 'email', 'is_staff', 'is_superuser','first_name','last_name','role')
    
admin.site.register(CustomUser, CustomUserAdmin)