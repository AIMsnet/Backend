from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse, redirect
from django.http import JsonResponse
#from .models import Supplier
from .forms import SupplierLogInForm
from Supplier.forms import SupplierProfileForm
from Supplier.models import Supplier 

import re #imported to check for password validatiors

# Create your views here.

def home(request, *args, **kwargs):
    supplierLogInForm = SupplierLogInForm()
    supplierProfileForm = SupplierProfileForm()
    context = {'supplierLoginForm' : supplierLogInForm, 'supplierProfileForm' : supplierProfileForm}
    return render(request, 'HomeTwo.html', context)

def supplierSignIn(request, *args, **kwargs):
    print('Insdide Method')
    return render(request, '/Supplier', {})


def supplierSignUp(request):
    print("Insdie Supplier Sign Up")
    full_name = request.POST['fullname']
    password = str(request.POST['password'])
    confirmPassword = str(request.POST['confirm_password'])
    # confirmPassword = str(request.POST.get('confirm_password', False))
    emailToVerify = request.POST['email']
    message = ''
    status = 0
    flag = True
    if(request.method == "POST"):
        try:
            if(len(password) < 8):
                flag = False
                message = 'Password must have length 8 or more than 8'
                status_code = 406
            elif not re.search("[a-z]", password):
                message = "Password must have atleast a small character"
                status_code = 406
                flag = False
            elif not re.search("[A-Z]", password): 
                message = "Password must have atleast a captial character"
                status_code = 406
                flag = False
            elif not re.search("[0-9]", password): 
                message = "Password must have atleast a number"
                status_code = 406
                flag = False
            elif (password != confirmPassword):
                message = "Password & Confirm password dosent match"
                status_code = 406
                flag = False
            elif Supplier.objects.filter(email = emailToVerify).exists():
                message = "You cannot register with this Email (Existing Email)"
                status_code = 406
                flag = False
        except Exception:
            print (Exception)

        if(flag):
            print("Inside true flag")
            Supplier.objects.create(full_name = full_name, email = emailToVerify, password = password)
            message = "Account Created"
            status_code = 201

    return JsonResponse(status = status_code, data = {'message':message})





        
        
        
        

