from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse, redirect
from django.http import JsonResponse
#from .models import Supplier
from .forms import SupplierLogInForm

#From app supplier
from Supplier.forms import SupplierProfileForm
from Supplier.models import Supplier 

#From app Customer
from Customer.forms import CustomerSignUpForm
from Customer.models import Customer

import re #imported to check for password validatiors

# Create your views here.

def home(request, *args, **kwargs):
    supplierLogInForm = SupplierLogInForm()
    supplierProfileForm = SupplierProfileForm()
    customerSignUpForm = CustomerSignUpForm

    context = {'supplierLoginForm' : supplierLogInForm, 'supplierProfileForm' : supplierProfileForm, 'customerSignUpForm' : customerSignUpForm}
    return render(request, 'HomeTwo.html', context)

def supplierSignUp(request):
    full_name = request.POST['fullname']
    password = str(request.POST['password'])
    confirmPassword = str(request.POST['confirm_password'])
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
            Supplier.objects.create(full_name = full_name, email = emailToVerify, password = password)
            message = "Account Created"
            status_code = 201
    
    return JsonResponse(status = status_code, data = {'message':message})


def supplierSignIn(request, *args, **kwargs):
    if(request.method == "POST"):
        email = request.POST['email']
        password = request.POST['password']

        if Supplier.objects.filter(email = email).exists():
            supplier = Supplier.objects.get(email = email)
            print(supplier.password)
            if(supplier.password == password):
                return render(request, '/Supplier')
            else:
                message = "Invalid Password !"
                status_code = 401
                return JsonResponse(status = status_code, data = {'message':message})
        else:
                message = "No Account Found"
                status_code = 401
                return JsonResponse(status = status_code, data = {'message':message})

def customerSignUp(request):
    print("Inside Customer Sign Up")
    if(request.method == "POST"):
        fullName = request.POST['fullName']
        mobileNumber = request.POST['mobileNumber']
        address = request.POST['address']
        taluka = request.POST['taluka']
        post = request.POST['post']
        district = request.POST['district']

        if Customer.objects.filter(mobile_number = mobileNumber).exists():
            message = "You cannot register with this number (Already Existing)"
            status_code = 406
        else :
            Customer.objects.create(
                full_name = fullName,
                mobile_number = mobileNumber,
                address = address,
                taluka = taluka,
                post = post,
                district = district
            )
            message = "Account Created"
            status_code = 200
    print(message)
    print(status_code)
    return JsonResponse(status = status_code, data = {'message':message})
    

def customerSignIn(request):
    if(request.method == "POST"):
        mobileNumber = request.POST['contact']

        if Customer.objects.filter(mobile_number = mobileNumber).exists():
            message = "Successfull Login"
            status_code = 200
        else :
            message = "No User found with this Mobile Number"
            status_code = 401
    return JsonResponse(status = status_code, data = {'message':message})