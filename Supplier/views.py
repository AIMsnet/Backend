from django.shortcuts import render
from .models import Supplier 
from .forms import SupplierProfileForm

# Create your views here.

def showSupplier(request, *args,**kwargs):
    # if (request.method == "POST"):
    #     supplierProfileForm = SupplierProfileForm(request.POST)
    #     if(supplierProfileForm.is_valid()):
    #         supplierProfileForm.save()
    #     else:
    #         print(supplierProfileForm.errors)
    #     return render(request, 'SupplierProfile.html')
    # else:
    #     supplierProfileForm = SupplierProfileForm()
    #     context = {'supplierProfileForm' : supplierProfileForm}
    return render(request, 'SupplierProfile.html')