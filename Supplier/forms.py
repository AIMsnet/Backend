from django import forms
from . import models

class SupplierProfileForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs = {
            'id' : "confirmPassword",
            'class' : 'form-control',
            'placeholder' : 'Confirm Password'
        }
    ))

    class Meta:
        model = models.Supplier
        fields = ("full_name","phone_number","mobile_number", "email",
                  "password", "email_optional", "address", 
                  "area_street", "city", "district", "taluka", "state",
                  "pincode", "designation")
        widgets = {
                'full_name' : forms.TextInput(attrs = {'id' : 'firstName' ,'class' : 'form-control', 'placeholder' : 'First Name'}),
                'designation' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Designation'}),
                'phone_number' : forms.NumberInput(attrs = {'class' : 'form-control', 'placeholder' : 'Phone Number'}),
                'mobile_number' : forms.NumberInput(attrs = {'class' : 'form-control', 'placeholder' : 'Mobile Number'}),
                'email' : forms.EmailInput(attrs = {'id' : 'email', 'class' : 'form-control', 'placeholder' : 'Email'}),
                'password' : forms.PasswordInput(attrs = {'id' : 'supplierPassword', 'class' : 'form-control', 'placeholder' : 'Password'}),
                'email_optional' : forms.EmailInput(attrs = {'class' : 'form-control', 'placeholder' : 'Optional Email'}),
                'address' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Address'}),
                'area_street' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Area/Street'}),
                'city' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'City'}),
                'district' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'District'}),
                'taluka' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Taluka'}),
                'state' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'state'}),
                'pincode' : forms.NumberInput(attrs = {'class' : 'form-control', 'placeholder' : 'Pincode'}),
        }