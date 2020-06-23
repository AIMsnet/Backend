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
    
    ownershipType = [('Proprietor', 'Proprietor'),
                     ('Partnership Firm', 'Partnership Firm'),
                     ('Limited Company (Ltd/Pvt.Ltd)', 'Limited Company (Ltd/Pvt.Ltd)'),
                     ('Limited Liability Partnership (LLP)', 'Limited Liability Partnership (LLP)')]
    
    ownership_type = models.CharField(max_length = 255, blank = False, null = False, choices = ownershipType)
    businessType = [('Manufacturer', 'Manufacturer'), 
                    ('Exporter', 'Exporter'),
                    ('Wholesale Distributor', 'Wholesale Distributor'), 
                    ('Wholesale Seller', 'Wholesale Seller'),
                    ('Wholesale Supplier', 'Wholesale Supplier'), 
                    ('Wholesale Trader', 'Wholesale Trader'),
                    ('Authorized Distributor', 'Authorized Distributor'), 
                    ('Channel Partner', 'Channel Partner'), 
                    ('Retailer', 'Retailer')]
    business_type = models.CharField(max_length = 255, blank = False, null = False, choices = businessType)
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
    image = models.FileField(upload_to = 'ProductImage', default = "")
    name = models.CharField(max_length = 255, null = False, blank = False)
    price = models.DecimalField(null = False, blank = False)
    arrivalChoices = [('Yes', 'Yes'), ('No', 'No')]
    arrival = models.CharField(max_length = 255, blank = False, null = False, choices = arrivalChoices, default = "")
    unitChoices = [('meter', 'meter'),
             ('Kg', 'Kg'),
             ('pack', 'pack'),
             ('unit', 'unit')]
    unit = models.CharField(max_length = 255, blank = False, null = False, choices = unitChoices, default = "-")
    description = models.TextField(null = True, blank = True)
    main_category = models.CharField(max_length = 255, null = False, blank = False, default = "-")
    sub_main_category = models.CharField(max_length = 255, null = False, blank = False, default = "-")
    category = models.CharField(max_length = 255, null = False, blank = False, default = "-")
    brand = models.CharField(max_length = 255, null = False, blank = False, default = "-")
    code = models.CharField(max_length = 255, null = True, blank = False, default = "-")
    additional_information = models.TextField(null = True, blank = True)
    created_date = models.DateField(("DD/MM/YYYY"), auto_now_add=True)
    updated_date = models.DateField(("DD/MM/YYYY"), auto_now_add = False)
    price = models.DecimalField(decimal_places = 2, max_digits = 12, blank = False, null = False)
    clicks = models.DecimalField(decimal_places = 0, max_digits = 12, blank = False, null = False)
    requested_quote = models.DecimalField(max_digits = 64, decimal_places = 0, default = 0)
    business = models.ForeignKey(Business, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.pk) + '|' + self.name

class Main_Categories(models.Model):
    name = models.CharField(max_length = 255)
    image = models.FileField(upload_to = 'Pics')

    def __str__(self):
        return str(self.pk) + "|" + self.name
    

class Sub_Main_Category(models.Model):
    name = models.CharField(max_length = 255)
    main_categories = models.ForeignKey(Main_Categories, on_delete = models.CASCADE)
    image = models.FileField(upload_to = 'Pics')

    def __str__(self):
        return self.name + " | Main Category ==>  " + str(self.main_categories.pk)
    

class Category(models.Model):
    name = models.CharField(max_length = 255)
    sub_main_category = models.ForeignKey(Sub_Main_Category, on_delete = models.CASCADE)

    def __str__(self):
        return self.name + "| Sub Main ==>  " + str(self.sub_main_category.name)
    