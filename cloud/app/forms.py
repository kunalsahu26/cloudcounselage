from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from .models import Studeinfo

from .models import Studeinfo
class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username','email','password')
        # widgets = {
        #     'username': forms.CharField(attrs={'class': 'class1'}),
        #     'username': forms.CharField(attrs={'class': 'class2'}),
        #     'username': forms.CharField(attrs={'class': 'class3'}),
        # }
        widgets = {
            'username': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'john',
                'font-wight' : 'Bold'
                }),
            'email': forms.EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'john@gmail.com'
                })
        }

# class UserFormInfo(forms.ModelForm):
#     class Meta:
#         model=Studeinfo

class LoginForm(forms.Form):
    username=forms.CharField(max_length=227)
    password=forms.CharField(widget=forms.PasswordInput())
