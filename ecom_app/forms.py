from django import forms
from .models import *
from django.contrib.auth.models import AbstractUser


class shopform(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['username','first_name','last_name','email','password','is_shop','mobile_no',
                   'pin_code','address','profile_pic']
        exclude = ('is_shop',)
    
        widgets ={
                'username' : forms.TextInput(attrs={'class':'form-control'}),
                'first_name' : forms.TextInput(attrs={'class':'form-control'}),
                'last_name' : forms.TextInput(attrs={'class':'form-control'}),
                'password' : forms.PasswordInput(attrs={'class':'form-control'}),
                'email' : forms.EmailInput(attrs={'class':'form-control'}),
                'mobile_no' : forms.TextInput(attrs={'class':'form-control'}),
                'address' : forms.TextInput(attrs={'class':'form-control'}),
                
                'pin_code' : forms.TextInput(attrs={'class':'form-control'}),
        
        }

class customerform(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['username','first_name','last_name','email','password','is_customer','mobile_no',
                   'pin_code','address','profile_pic']
        exclude = ('is_customer',)
    
        widgets ={
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'mobile_no' : forms.TextInput(attrs={'class':'form-control'}),
            'address' : forms.TextInput(attrs={'class':'form-control'}),
    
            'pin_code' : forms.TextInput(attrs={'class':'form-control'}),
        }