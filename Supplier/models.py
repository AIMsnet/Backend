from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Supplier(models.Model):
    full_name = models.CharField(max_length=150, blank = False, null = False)
    phone_number = models.DecimalField(max_digits = 10, decimal_places = 0, blank=True, null = True)
    mobile_number = models.DecimalField(max_digits = 10, decimal_places = 0, blank = False, null = False)
    email = models.EmailField(max_length = 255, blank = False, null = False)
    password = models.CharField(max_length = 32, blank = False, null = False)
    email_optional = models.EmailField( default = "-", max_length = 255, blank = True)
    address = models.TextField(blank = False, null = False)
    area_street = models.TextField(blank = False, null = False)
    city = models.CharField(max_length = 255, blank = False, null = False)
    district = models.CharField(max_length = 255, blank = False, null = False)
    taluka = models.CharField(max_length = 255, blank = False, null = False)
    state = models.CharField(max_length = 255, blank = False, null = False)
    pincode = models.DecimalField(max_digits = 6, decimal_places = 0, blank = False, null = False)
    designation = models.CharField(max_length=255, blank = False, null = False, default = "")
    # organizationName 

    def __str__(self):
        return str(self.pk) + '|' + self.full_name

class Business(models.Model):
    name = models.CharField(max_length = 255, blank = False, null = False, default = '')
    organisation_type = models.CharField(max_length = 255, blank = False, null = False)
    ownership_type = models.CharField(max_length = 255, blank = False, null = False)
    business_type = models.CharField(max_length = 255, blank = False, null = False)
    business_email = models.EmailField(max_length = 255, blank = False, null = False)
    website_link = models.CharField(max_length = 255, blank = True, null = True)
    address = models.CharField(max_length = 255, blank = False, null = False)
    year_of_establishment = models.DateField(blank = False, null = False)
    description = models.TextField(blank = False, null = False)
    supplier = models.ForeignKey(Supplier, on_delete = models.CASCADE)
    GST = models.CharField(blank = False, null = False, max_length = 13, default = '')
    PAN = models.CharField(blank = False, null = False, max_length = 13, default = '')
    CIN = models.CharField(blank = False, null = False, max_length = 13, default = '')
    DGFT = models.CharField(blank = False, null = False, max_length = 13, default = '') 

    def __str__(self):
        return str(self.pk) + '|' + self.name
    

class Product(models.Model):
    name = models.CharField(max_length = 255)
    created_date = models.DateField(("DD/MM/YYYY"), auto_now = False, auto_now_add=True)
    updated_date = models.DateField(("DD/MM/YYYY"), auto_now = True, auto_now_add = False)
    category = models.CharField(max_length = 255, blank = False, null = False)
    price = models.DecimalField(decimal_places = 2, max_digits = 12, blank = False, null = False)
    clicks = models.DecimalField(decimal_places = 0, max_digits = 12, blank = False, null = False)
    business = models.ForeignKey(Business, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.pk) + '|' + self.name
    