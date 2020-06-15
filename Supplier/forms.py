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
                'full_name' : forms.TextInput(attrs = {'id' : 'fullName' ,'class' : 'form-control', 'placeholder' : 'First Name'}),
                'designation' : forms.TextInput(attrs = {'id' : 'desgination', 'class' : 'form-control', 'placeholder' : 'Designation'}),
                'phone_number' : forms.NumberInput(attrs = {'id' : 'phone_number', 'class' : 'form-control', 'placeholder' : 'Phone Number'}),
                'mobile_number' : forms.NumberInput(attrs = {'id' : 'mobile_number', 'class' : 'form-control', 'placeholder' : 'Mobile Number'}),
                'email' : forms.EmailInput(attrs = {'id' : 'email', 'class' : 'form-control', 'placeholder' : 'Email', 'readOnly' : 'True'}),
                'password' : forms.PasswordInput(attrs = {'id' : 'supplierPassword', 'class' : 'form-control', 'placeholder' : 'Password'}),
                'email_optional' : forms.EmailInput(attrs = {'id' : 'email_optional', 'class' : 'form-control', 'placeholder' : 'Optional Email'}),
                'address' : forms.TextInput(attrs={'id' : 'address', 'class' : 'form-control', 'placeholder' : 'Address'}),
                'area_street' : forms.TextInput(attrs={'id' : 'area_street', 'class' : 'form-control', 'placeholder' : 'Area/Street'}),
                'city' : forms.TextInput(attrs={'id' : 'city', 'class' : 'form-control', 'placeholder' : 'City'}),
                'district' : forms.TextInput(attrs={'id' : 'district', 'class' : 'form-control', 'placeholder' : 'District'}),
                'taluka' : forms.TextInput(attrs={'id' : 'taluka', 'class' : 'form-control', 'placeholder' : 'Taluka'}),
                'state' : forms.TextInput(attrs={'id' : 'state', 'class' : 'form-control', 'placeholder' : 'state'}),
                'pincode' : forms.NumberInput(attrs = {'id' : 'pincode', 'class' : 'form-control', 'placeholder' : 'Pincode'}),
        }

class BusinessProfileForm(forms.ModelForm):
    
    class Meta:
        model = models.Business
        fields = ("name", "organisation_type", "ownership_type",
            "business_type", "business_email", "website_link",
            "address", "year_of_establishment", "description",
            "GST", "PAN", "CIN",  "DGFT")

        widgets = {
            'name' : forms.TextInput(attrs = {'id' : 'name', 'class' : 'form-control', 'placeholder' : 'Name'}),
            'organisation_type' : forms.TextInput(attrs = {'id' : 'organisationType', 'class' : 'form-control', 'placeholder' : 'Ogranistaion Type'}),
            'ownership_type' : forms.Select(attrs = {'id' : 'ownershipType', 'class' : 'form-control', 'placeholder' : 'Ownership Type'}),
            'business_type' : forms.Select(attrs = {'id' : 'businessType', 'class' : 'form-control', 'placeholder' : 'Business Type'}),
            'business_email' : forms.TextInput(attrs = {'id' : 'businessEmail', 'class' : 'form-control', 'placeholder' : 'Business Email'}),
            'website_link' : forms.TextInput(attrs = {'id' : 'websiteLink', 'class' : 'form-control', 'placeholder' : 'Website Link'}),
            'address' : forms.TextInput(attrs = {'id' : 'address', 'class' : 'form-control', 'placeholder' : 'Address'}),
            'year_of_establishment' : forms.DateInput(attrs = {'id' : 'establishment', 'class' : 'form-control', 'placeholder' : 'Year Of Establishment','type' : 'date'}),
            'description' : forms.TextInput(attrs = {'id' : 'description', 'class' : 'form-control', 'placeholder' : 'Description of Company'}),
            'GST' : forms.TextInput(attrs = {'id' : 'GST', 'class' : 'form-control', 'placeholder' : 'GST'}),
            'PAN' : forms.TextInput(attrs = {'id' : 'PAN', 'class' : 'form-control', 'placeholder' : 'PAN'}),
            'CIN' : forms.TextInput(attrs = {'id' : 'CIN', 'class' : 'form-control', 'placeholder' : 'CIN'}),
            'DGFT' : forms.TextInput(attrs = {'id' : 'DGFT', 'class' : 'form-control', 'placeholder' : 'DGFT'}),
        }