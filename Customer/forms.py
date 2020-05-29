from  django import forms
from .import models

class CustomerSignUpForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = ("full_name","mobile_number", "address", "taluka", "post", "district")
        widgets = {
                    'full_name' : forms.TextInput(attrs = {'id' : 'full_name' ,'class' : 'form-control', 'placeholder' : 'First Name'}),
                    'mobile_number' : forms.NumberInput(attrs = {'id' : 'mobile_number', 'class' : 'form-control', 'placeholder' : 'Mobile Number'}),
                    'address' : forms.TextInput(attrs={'id' : 'address', 'class' : 'form-control', 'placeholder' : 'Address'}),
                    'taluka' : forms.TextInput(attrs={'id' : 'taluka', 'class' : 'form-control', 'placeholder' : 'Taluka'}),
                    'post' : forms.TextInput(attrs = {'id' : 'post', 'class' : 'form-control', 'placeholder' : 'Post'}),
                    'district' : forms.TextInput(attrs={'id' : 'district','class' : 'form-control', 'placeholder' : 'District'}),
                 }