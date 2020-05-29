from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Customer(models.Model):
    full_name = models.CharField(max_length = 32, blank = False, null = False)
    mobile_number = models.DecimalField(null = False, blank = False, decimal_places = 0, max_digits = 12)
    address = models.TextField(blank = False, null = False)
    taluka = models.TextField(blank = False, null = False)
    post = models.TextField(blank = False, null = False)
    district = models.TextField(blank = False, null = False)

    def __str__(self):
        return str(self.pk) + self.full_name 
    