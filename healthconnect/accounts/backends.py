from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class EmailBackend(ModelBackend):
   
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None or password is None:
            return None

        User = get_user_model()
        try:
            user = User.objects.get(email=username)  # Use email for login
            if user.check_password(password):  # Check password
                return user
        except User.DoesNotExist:
            return None
