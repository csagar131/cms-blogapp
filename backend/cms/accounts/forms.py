from django.contrib.auth.forms import UserCreationForm
from django import forms
from accounts.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','image','password1','password2','is_author')


class UpdateProfileForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('first_name','last_name','email','bio','image','is_author')
