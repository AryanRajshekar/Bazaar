from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# User is inbuilt in Django with username password and email
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    # no need of class Meta and model=User in login form because we are using default Django Auth form
    username= forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class':'w-full py-4 px-6 rounded-xl'
    }
    ))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class':'w-full py-4 px-6 rounded-xl'
    }
    ))


class SignupForm(UserCreationForm):
    # we are extending the signupform class with UserCreationForm
    # class Meta used for basic behaviour
    class Meta:
        # since we are using the default user from Django Auth system
        # also we have to create a model to let Django know from where it should take the fields
        model=User
        fields=('username','email','password1','password2')
    # in django UserCreationForm only certain conditions for username and pwd are available
    username= forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class':'w-full py-4 px-6 rounded-xl'
    }
    ))
    # widgets should be in class meta
    # if you change one input as the one given below you have to change all or they become seperate divs since 
    # represent different stylings and fields
    # widgets = {
    #     'email': forms.EmailInput(attrs={
    #         'class': 'w-full py-4 px-6 rounded-xl'
    #     })
    # }
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class':'w-full py-4 px-6 rounded-xl'
    }
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class':'w-full py-4 px-6 rounded-xl'
    }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat Password',
        'class':'w-full py-4 px-6 rounded-xl'
    }
    ))