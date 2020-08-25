from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Supplier)
admin.site.register(models.Business)
admin.site.register(models.Product)
admin.site.register(models.Main_Categories)
admin.site.register(models.Sub_Main_Category)
admin.site.register(models.Category)
admin.site.register(models.Quote)