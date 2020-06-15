from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.shortcuts import render
from .models import Supplier, Business, Main_Categories
from .forms import SupplierProfileForm, BusinessProfileForm
from django.core import serializers
import json
import re

# Create your views here.
def returnPage(request):
    businessProfileForm = BusinessProfileForm()
    email = request.session.get('email', False)
    business = None
    designation = None
    mainCategories = None
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
        businessProfileForm = BusinessProfileForm(initial = {
        'name' : business.name, 'organisation_type' : business.organisation_type,
        'ownership_type' : business.ownership_type, 'business_type' : business.business_type,
        'business_email' : business.business_email, 'website_link' : business.website_link,
        'address' : business.address, 'year_of_establishment' : business.year_of_establishment,
        'description' : business.description, 'GST' : business.GST, 'PAN' : business.PAN, 'CIN' : business.CIN,
        'DGFT' : business.DGFT
    })
        mainCategories = Main_Categories.objects.all()
        print("These are main categories-----------", mainCategories)
    except Exception as e:
        business = "Not Found"
    
    if supplier.designation == "":
        designation = "Not Found"
  
    context = {
        'supplier' : supplier,
        'business' : business,
        'designation' : designation,
        'supplierProfileForm' : supplierProfileForm,
        'businessProfileForm' : businessProfileForm,
        'mainCategories' : mainCategories
    }
    print("Redirected")
    return render(request, 'SupplierProfile.html', context)


def personalUpdate(request):
    if request.method == 'POST':
        flag = True
        email = request.session.get('email')
        if(request.POST['request'] == "Update"):
            supplier = Supplier.objects.get(email = email)
            supplier.full_name = request.POST['fullName']   
            supplier.email_optional = request.POST['emailOptional']
            supplier.address = request.POST['address']
            supplier.area_street = request.POST['area']
            supplier.city = request.POST['city']
            supplier.district = request.POST['district']
            supplier.taluka = request.POST['taluka']
            supplier.state = request.POST['state']
            supplier.pincode = request.POST['pincode']
            supplier.save()
            supplier = serializers.serialize('json', [supplier])
            y = json.loads(supplier)
            y = y[0]['fields']
            response = {'status': 0, 'message': ("Details Updated"), 'supplier': y} 
            return HttpResponse(json.dumps(response), content_type='application/json')
        else:
            phone = request.POST['phone']
            mobile = request.POST['mobile']
            emailOptional = request.POST['emailOptional']
            address = request.POST['address']
            area = request.POST['area']
            city = request.POST['city']
            district = request.POST['district']
            taluka = request.POST['taluka']
            state = request.POST['state']
            pincode = request.POST['pincode']
            designation = request.POST['designation']
            if(len(mobile) != 10 or re.match("^[6-9]\d{9}$", mobile) == None):
                flag = False
                response = {'status' : 1, 'message' : ("Invalid Mobile Number !")}
            elif(len(pincode) != 6):
                flag = False
                response = {'status' : 1, 'message' : ("Invali Pincode!")}
            elif(email == emailOptional):
                flag = False
                response = {'status' : 1, 'message' : ("Email and Optional Email cannot be same!")}
            if(flag):
                supplier = Supplier.objects.get(email = email)
                supplier.phone_number = phone
                supplier.mobile_number = mobile
                supplier.email_optional = emailOptional
                supplier.address = address
                supplier.area_street = area
                supplier.city = city
                supplier.district = district
                supplier.taluka = taluka
                supplier.state = state
                supplier.pincode = pincode
                supplier.designation = designation
                supplier.save()
                response = {'status': 0, 'message': ("Details Updated")}
                
                if Business.objects.filter(supplier = supplier).exists():
                    response = {'status': 0, "profileComplete" : "0","email" : email,'message': ("Details Updated")}    
                else:
                    response = {'status': 0, "profileComplete" : "1",'message': ("Details Updated")}
        return HttpResponse(json.dumps(response), content_type='application/json')

def businessUpdate(request):
    if request.method == 'POST':
        supplierEmail = request.session.get('email')
        if request.POST['request'] == "Update":
            businessType = request.POST['businessType']
            businessEmail = request.POST['businessEmail']
            organisationType = request.POST['organisationType']
            ownershipType = request.POST['ownershipType']
            websiteLink = request.POST['websiteLink']
            address = request.POST['address']
            supplier = Supplier.objects.get(email = supplierEmail)
            business = Business.objects.get(supplier = supplier)
            business.business_type = businessType
            business.business_email = businessEmail
            business.organisation_type = organisationType
            business.ownership_type = ownershipType
            business.website_link = websiteLink
            business.address = address

            business.save()

            business = serializers.serialize('json', [business])
            y = json.loads(business)
            y = y[0]['fields']
            response = {'status': 0, 'message': ("Details Updated"), 'business': y} 
            return HttpResponse(json.dumps(response), content_type='application/json')

        else:
            name = request.POST['name']
            organisationType = request.POST['organisationType']
            ownershipType = request.POST['ownershipType']
            businessType = request.POST['businessType']
            businessEmail = request.POST['businessEmail']
            websiteLink = request.POST['websiteLink']
            address = request.POST['address']
            establishment = request.POST['establishment']
            description = request.POST['description']
            GST = request.POST['GST']
            PAN = request.POST['PAN']
            CIN = request.POST['CIN']
            DGFT = request.POST['DGFT']

            supplier = Supplier.objects.get(email = supplierEmail)

            try:
                business = Business.objects.get(supplier = supplier)
                business.business_type = businessType
                business.business_email = businessEmail
                business.organisation_type = organisationType
                business.ownership_type = ownershipType
                business.website_link = websiteLink
                business.address = address
                business.year_of_establishment = establishment
                business.description = description
                business.save()
                response = {'status': 0, 'message': ("Details Updated")}
            except Exception as identifier:
                Business.objects.create(name = name, organisation_type = organisationType,
                ownership_type = ownershipType, business_type = businessType,
                business_email = businessEmail, website_link = websiteLink, address = address,
                year_of_establishment = establishment, supplier = supplier,
                description = description, GST = GST, PAN = PAN, CIN = CIN,
                DGFT = DGFT)
                response = {'status': 0, 'message': ("Details Updated")}

    
            if supplier.designation != "":
                response = {'status': 0, "profileComplete" : "0", "email" : supplierEmail,'message': ("Details Updated")}
            else:
                response = {'status': 0, "profileComplete" : "1",'message': ("Details Updated")}
            
            return HttpResponse(json.dumps(response), content_type='application/json')
