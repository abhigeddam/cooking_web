from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username','email','password1','password2']
        error_messages = {
            'password1': {
                'unique': 'Password must contain atleast 8 keys and special letters !!!',
            },

        }
    error_messages = {
        'password_mismatch': "Your Password Mismatch For 'UserCreationForm' class",
    }