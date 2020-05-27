from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse, redirect
#from .models import Supplier
from .forms import SupplierLogInForm
from Supplier.forms import SupplierProfileForm
from Supplier.models import Supplier 

# Create your views here.

def home(request, *args, **kwargs):
    print("Inside Home Inside Home Inside Home Inside Home Inside Home Inside Home ")
    if(request.method == "POST"):
        supplierLogInForm = SupplierLogInForm(request.POST)
        if (supplierLogInForm.is_valid()):
            print(supplierLogInForm.cleaned_data)
            response = redirect('/Supplier')
            return response
    else:
        supplierLogInForm = SupplierLogInForm()
        supplierProfileForm = SupplierProfileForm()
        context = {'supplierLoginForm' : supplierLogInForm, 'supplierProfileForm' : supplierProfileForm}
        return render(request, 'HomeTwo.html', context)

def supplierSignIn(request, *args, **kwargs):
    print('Insdide Method')
    return render(request, '/Supplier', {})


def supplierSignUp(request, *args, **kwargs):
    if(request.method == "POST"):
        # if(request.POST['password'] == request.POST['confirm_password'])
        Supplier.objects.create(
            fullname = request.POST['full_name'],
            email = request.POST['email'],
            password = request.POST['password']
        )
        return HttpResponse('')
        
        
        

