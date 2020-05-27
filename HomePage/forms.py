from django import forms
from . import models

class SupplierLogInForm(forms.ModelForm):
    
    username = forms.CharField(widget=forms.TextInput(
        attrs = {
            'id' : "username",
            'class' : 'form-control supplierSignInFormControl',
            'placeholder' : 'Username'
        }
    ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'id' : 'password',
            'class' : 'form-control supplierSignInFormControl',
            'placeholder' : 'password'

        }
    ))

    class Meta:
        model = models.Supplier
        fields = ("username", "password",)