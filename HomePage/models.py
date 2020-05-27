from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Supplier(models.Model):
    username = models.CharField(max_length=200)
    password = models.TextField()

    def __str__(self):
        return self.username + '|' + str(self.pk)