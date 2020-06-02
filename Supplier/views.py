from django.shortcuts import render
from .models import Supplier, Business
from .forms import SupplierProfileForm

# Create your views here.

def showSupplier(request, email):
    if (request.method == "POST"):
        supplierProfileForm = SupplierProfileForm(request.POST)
        if(supplierProfileForm.is_valid()):
            supplierProfileForm.save()
        else:
            print(supplierProfileForm.errors)
        return render(request, 'SupplierProfile.html')
    else:
        
        business = None
        supplier = Supplier.objects.get(email = email)
        supplierProfileForm = SupplierProfileForm(initial=
        {'full_name' : supplier.full_name, 'designation' : supplier.designation,
            'phone_number' : supplier.phone_number, 'mobile_number' : supplier.mobile_number,
            'email' : supplier.email, 'email_optional' : supplier.email_optional,
            'address': supplier.address, 'area_street' : supplier.area_street, 'city' : supplier.city,
            'district' : supplier.district, 'taluka' : supplier.taluka, 'state' : supplier.state,
            'pincode' : supplier.pincode
        })
        try:
            
           
            business = Business.objects.get(supplier = supplier)
        except Exception:
            print(Exception)
            business = "Not Found"
    
        context = {
            'supplier' : supplier,
            'business' : business,
            'supplierProfileForm' : supplierProfileForm
        }
        
        print("Supplier Forigen object", business)
    return render(request, 'SupplierProfile.html', context)

# def 