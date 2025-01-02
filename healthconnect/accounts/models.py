from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('healthcare_provider', 'Healthcare Provider'),
        ('patient', 'Patient'),
        ('admin', 'Admin'),
        ('other_staff', 'Other Staff'),
    ]
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, default='patient')
    email = models.EmailField(unique=True)  # Make email unique

    def __str__(self):
        return f"{self.username} ({self.role})"
    
    def save(self, *args, **kwargs):
        if self.is_superuser:  # If the user is a superuser, assign them the 'admin' role
            self.role = 'admin'
        super().save(*args, **kwargs)
    # Use email as the primary field for authentication
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Optional: includes 'username' when creating superusers, but not for login
