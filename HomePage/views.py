from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse, redirect
#from .models import Supplier
from .forms import SupplierLogInForm

#From app supplier
from Supplier.forms import SupplierProfileForm
from Supplier.models import Supplier, Product

#From app Customer
from Customer.forms import CustomerSignUpForm
from Customer.models import Customer

import re #imported to check for password validatiors
import json #imported for json dumps
# Create your views here.

#Random record
from random import sample

def home(request, *args, **kwargs):
    farmingTool = Product.objects.filter(main_category = 1)
    farmingTool = sample(list(farmingTool), min(len(farmingTool), 5))
    
    flowerPlant = Product.objects.filter(main_category = 2)
    flowerPlant = sample(list(flowerPlant), min(len(flowerPlant), 5))

    seedsPlan = Product.objects.filter(main_category = 3)
    seedsPlan = sample(list(seedsPlan), min(len(seedsPlan), 5))
    
    tractor = Product.objects.filter(main_category = 4)
    tractor = sample(list(tractor), min(len(tractor), 5))

    birdPoultry = Product.objects.filter(main_category = 5)
    birdPoultry = sample(list(birdPoultry), min(len(birdPoultry), 5))


    irrigationHarvesting = Product.objects.filter(main_category = 5)
    irrigationHarvesting = sample(list(irrigationHarvesting), min(len(irrigationHarvesting), 6))
  
    fertilizerSoil = Product.objects.filter(main_category = 7)
    fertilizerSoil = sample(list(fertilizerSoil), min(len(fertilizerSoil), 5))

    coirAgro = Product.objects.filter(main_category = 8)
    coirAgro = sample(list(coirAgro), min(len(coirAgro), 5))

    farmingPet = Product.objects.filter(main_category = 9)
    farmingPet = sample(list(farmingPet), min(len(farmingPet), 5))

    newArrival = Product.objects.filter(arrival = "Yes")
    newArrival = sample(list(newArrival), min(len(newArrival), 5))
    print("New Arrivals are -------------------------------\n", newArrival)

    context = {
        "farmingTool" : farmingTool,
        "flowerPlant" : flowerPlant,
        "seedsPlan" : seedsPlan,
        "tractor" : tractor,
        "birdPoultry" : birdPoultry,
        "irrigationHarvesting" : irrigationHarvesting,
        "fertilizerSoil" : fertilizerSoil,
        "coirAgro" : coirAgro,
        "farmingPet" : farmingPet,
        "newArrival" : newArrival
    }
    return render(request, 'HomeTwo.html', context)

def supplierSignUp(request):
    full_name = request.POST['fullname']
    password = str(request.POST['password'])
    confirmPassword = str(request.POST['confirm_password'])
    emailToVerify = request.POST['email']
    flag = True
    if(request.method == "POST"):
        try:
            if(len(password) < 8):
                flag = False
                response = {'status': 1, 'message': ("Password must have length 8 or more than 8")}
            elif not re.search("[a-z]", password):
                flag = False
                response = {'status': 1, 'message': ("Password must have atleast a small character")}
            elif not re.search("[A-Z]", password): 
                flag = False
                response = {'status': 1, 'message': ("Password must have atleast a captial character")}
            elif not re.search("[0-9]", password): 
                flag = False
                response = {'status': 1, 'message': ("Password must have atleast a number")}
            elif (password != confirmPassword):
                flag = False
                response = {'status': 1, 'message': ("Password & Confirm password dosent match")}
            elif Supplier.objects.filter(email = emailToVerify).exists():
                flag = False
                response = {'status': 1, 'message': ("You cannot register with this Email (Existing Email)")}
        except Exception:
            print (Exception)

        if(flag):
            Supplier.objects.create(full_name = full_name, email = emailToVerify, password = password)
            response = {'status': 0, 'message': ("Account Created")}

    return HttpResponse(json.dumps(response), content_type='application/json')


def supplierSignIn(request, *args, **kwargs):
    if(request.method == "POST"):
        print("After Passwordd-------------------------------------------------", request.POST['email'])
        email = request.POST['email']
        password = request.POST['password']
        if Supplier.objects.filter(email = email).exists():
            supplier = Supplier.objects.get(email = email)
            if(supplier.password == password):
                request.session['email'] = email
                location = '/Supplier/'
                response = {'status': 0, 'supplier': location}                
            else:
                response = {'status': 1, 'message': ("Invalid Password")}
        else:
                response = {'status': 1, 'message': ("No Account Found")}
    
    return HttpResponse(json.dumps(response), content_type='application/json')


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
            response = {'status': 0, 'message': ("You cannot register with this number (Already Existing)")}
        else :
            Customer.objects.create(
                full_name = fullName,
                mobile_number = mobileNumber,
                address = address,
                taluka = taluka,
                post = post,
                district = district
            )
            response = {'status': 0, 'message': ("Account Created")}
    return HttpResponse(json.dumps(response), content_type='application/json')


def customerSignIn(request):
    if(request.method == "POST"):
        mobileNumber = request.POST['contact']
        if Customer.objects.filter(mobile_number = mobileNumber).exists():
            response = {'status': 1, 'message': ("Successfull Login")}
            request.session['customer'] = mobileNumber
        else :
            response = {'status': 1, 'message': ("No User found with this Mobile Number")}

    return HttpResponse(json.dumps(response), content_type='application/json')

def customerSignOut(request):
    request.session.pop('customer')
    return redirect('homepage:landingPage')


def GovermentQuick(request):
    return render(request, 'GovermentLink.html')