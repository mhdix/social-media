from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class UserRegisterForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'ex@gmail.com'}))
    email2 = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'ex@gmail.com'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'mhdix ...'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'1234 ...'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':''}))
    
    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email = email)
        if user:
            raise ValidationError('this email already exist')
        return email
    
    def clean_username(self):
        print(self.cleaned_data['username'])
        username = self.cleaned_data['username']
        user = User.objects.filter(username = username).exists()
        if user:
            raise ValidationError('this username already exist')
        return username   

        
    def clean(self):
        cd = super().clean()
        pass1 = cd.get('password')
        pass2 = cd.get('confirm_password')
        
        if pass1 and pass2 and pass1 != pass2:
            raise ValidationError('password not matched')
        
        
        
class UserLoginForm(forms.Form):
    username = forms.CharField(label='نام کاربری', widget=(forms.TextInput(attrs={'placeholder':'نام کاربری'})))
    password = forms.CharField(widget=(forms.PasswordInput(attrs={'placeholder':'pass'})))
    
    