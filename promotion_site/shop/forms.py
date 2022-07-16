from django import forms
from models import *


class RegisterUser(forms.Form):
    email = forms.EmailField(max_length=100)
    nickname = forms.CharField(max_length=20)
    password = forms.PasswordInput(render_value=True)
