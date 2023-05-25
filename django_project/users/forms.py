from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # these class meta gives a nested name space of configurations
    # ad keeps the configurations in one place
    class meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
 