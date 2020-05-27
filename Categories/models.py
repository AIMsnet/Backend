from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Categories(models.Model):
    image = models.FileField(upload_to = 'Pics')
    name = models.CharField(max_length = 255, null = False, blank = False)

    def __str__(self):
        return self.name

class Sub_Categories(models.Model):
    name = models.CharField(max_length = 255, null = False, blank = False)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    sub_categories = models.CharField(max_length = 255, null = False, blank = False)
    category = models.ForeignKey(Categories, on_delete = models.CASCADE, default = '')

    def __str__(self):
        return self.name + "    |   " + self.sub_categories