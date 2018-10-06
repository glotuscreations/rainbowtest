from django.contrib.auth.models import User
from django import forms
from captcha.fields import CaptchaField

class SignUpForm(forms.ModelForm):

    captcha = CaptchaField()
    password = forms.CharField(max_length= 15, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
