from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render
from .models import Supplier, Business, Main_Categories, Sub_Main_Category, Category, Product, Quote
from .forms import SupplierProfileForm, BusinessProfileForm
from django.core import serializers
import json
import re
from django.utils import timezone
from django.db.models import Sum


# Create your views here.
def returnPage(request):
    businessProfileForm = BusinessProfileForm()
    email = request.session.get('email', False)
    business = None
    designation = None
    mainCategories = None
    product = None
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
    except Exception as e:
        business = "Not Found"
    
    if supplier.designation == "":
        designation = "Not Found"

    if designation !=  "Not Found" and business!= "Not Found":
        product = Product.objects.filter(business = business)
        quotes = Quote.objects.filter(supplier = supplier)
        leads = len(quotes)
        clicks = Product.objects.filter(business = business).aggregate(Sum('clicks'))
        productCount = len(product)
        profileViews = business.profile_views
    context = {
        'supplier' : supplier,
        'business' : business,
        'designation' : designation,
        'supplierProfileForm' : supplierProfileForm,
        'businessProfileForm' : businessProfileForm,
        'mainCategories' : mainCategories,
        "products" : product,
        "quotes" : quotes,
        "leads" : leads,
        "clicks" : clicks,
        "productCount" : productCount,
        "profileViews" : profileViews
    }
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

def addProduct(request):
    if request.method == "POST":
        print(request.POST, request.FILES)
        productImage = request.FILES['product_image']
        productName = request.POST['product_name']
        productBrand = request.POST['product_brand']
        productCode = request.POST['product_code']
        productPrice = request.POST['prodcut_price']
        productArrival = request.POST['prodcut_arrival']
        productUnit = request.POST['prodcut_unit']
        productDescription = request.POST['product_description']
        productMainCategory = request.POST['main_category']
        productSubMainCategory = request.POST['sub_main_category']
        productCategory = request.POST['category']
        productAdditionalInfo = request.POST['product_additional_information']  
        specification = []
        description = []
        for i in range(1, 11) :
            specification.append(request.POST.get('specification_' + str(i), None))

        for i in range(1, 11) :
            description.append(request.POST.get('description_' + str(i), None))
            
            
        print("Desc--------", description[0])
        supplierEmail = request.session.get('email', False)
        supplier = Supplier.objects.get(email = supplierEmail)
        business = Business.objects.get(supplier = supplier)
        product = Product.objects.create(image = productImage, name = productName, price = productPrice, 
        arrival = productArrival, unit = productUnit, description = productDescription,
        main_category = productMainCategory, sub_main_category = productSubMainCategory,
        category = productCategory, brand = productBrand, code = productCode, additional_information = productAdditionalInfo,
        created_date = timezone.now(), updated_date = timezone.now(), clicks = 0, business = business,
        specification_1 = specification[0], specification_2 = specification[1], specification_3 = specification[2],
        specification_4 = specification[3], specification_5 = specification[4], specification_6 = specification[5], 
        specification_7 = specification[6], specification_8 = specification[7], specification_9 = specification[8], 
        specification_10 = specification[9],description_1 = description[0], description_2 = description[1],
        description_3 = description[2], description_4 = description[3], description_5 = description[4], 
        description_6 = description[5], description_7 = description[6], description_8 = description[7],
        description_9 = description[8], description_10  = description[9], 
        )
        response = {'status': 0, 'code' : productCode, 'name' : productName
        ,'category' : productCategory,'price' : productPrice, 'arrival' : productArrival,
        'unit' : productUnit, 'brand' : productBrand, 'clicks' : str(0),
        'createDate' : product.created_date.strftime("%m%d%y")}
        return HttpResponse(json.dumps(response), content_type='application/json')

def updateProduct(request):
    print("Inside Update Product------------")
    print()
    if request.method == "POST":
        productImage = request.FILES['update_product_image']
        productName = request.POST['update_product_name']
        productBrand = request.POST['update_product_brand']
        productCode = request.POST['update_product_code']
        productPrice = request.POST['update_prodcut_price']
        productArrival = request.POST['update_prodcut_arrival']
        productUnit = request.POST['update_prodcut_unit']
        productDescription = request.POST['update_product_description']
        productMainCategory = request.POST['update_main_category']
        productSubMainCategory = request.POST['update_sub_main_category']
        productCategory = request.POST['update_category']
        productAdditionalInfo = request.POST['update_product_additional_information']
        specification = []
        description = []

        for i in range(1, 11) :
            specification.append(request.POST.get('updateSpecification_' + str(i), None))

        for i in range(1, 11) :
            description.append(request.POST.get('updateDescription_' + str(i), None))

        print("Description fro update", specification[0])

        supplierEmail = request.session.get('email')
        supplier = Supplier.objects.get(email = supplierEmail)
        business = Business.objects.get(supplier = supplier)
        product = Product.objects.filter(business = business).filter(code = productCode)
        product = product[0]
        creationDate = product.created_date
        product.image = productImage
        product.name = productName
        product.brand = productBrand
        product.code = productCode
        product.price = productPrice
        product.arrival = productArrival
        product.unit = productUnit
        product.description = productDescription
        product.main_category = productMainCategory
        product.sub_main_category = productSubMainCategory
        product.category = productCategory
        product.additional_information =  productAdditionalInfo
        product.update_date = timezone.now()
        product.specification_1 = specification[0]
        product.specification_2 = specification[1]
        product.specification_3 = specification[2]
        product.specification_4 = specification[3]
        product.specification_5 = specification[4]
        product.specification_6 = specification[5]
        product.specification_7 = specification[6]
        product.specification_8 = specification[7]
        product.specification_9 = specification[8]
        product.specification_10 = specification[9]

        product.description_1 = description[0]
        product.description_2 = description[1]
        product.description_3 = description[2]
        product.description_4 = description[3]
        product.description_5 = description[4]
        product.description_6 = description[5]
        product.description_7 = description[6]
        product.description_8 = description[7]
        product.description_9 = description[8]
        product.description_10 = description[9]
        
        product.save()
        print("Date berfore str", creationDate)
        print("This is created date", creationDate.strftime("%m%d%y"))
        response = {'status': 0, 'code' : productCode, 'name' : productName
        ,'category' : productCategory,'price' : productPrice, 'arrival' : productArrival,
        'unit' : productUnit, 'brand' : productBrand, 'clicks' : str(product.clicks),
        'createDate' : product.created_date.strftime("%m%d%y")}
        return HttpResponse(json.dumps(response), content_type='application/json')
    
def getCategory(request):
    category = ""
    if request.method == "POST":
        value = request.POST['value']
        if request.POST['request'] == "sub":
            subCategory = Sub_Main_Category.objects.filter(main_categories = value)
            subCategory = serializers.serialize('json', subCategory)
            subCategory = json.loads(subCategory)
            response = {'subCategory' : subCategory}
        elif request.POST['request'] == "category":
            subMainCategory = Sub_Main_Category.objects.get(name = value)
            category = Category.objects.filter(sub_main_category = subMainCategory)
            category = serializers.serialize('json', category)
            category = json.loads(category)
            response = {'category' : category}
    return HttpResponse(json.dumps(response), content_type = 'application/json')
        
def getCategoryUpdate(request):
    if request.method == "POST":
        limit = 0
        categoryName = request.POST['category']
        print("Category Name from Updateee", categoryName)
        category = Category.objects.get(name = categoryName)
        print("Sub Category got Name ------------", category.sub_main_category.name)
        subCategory = Sub_Main_Category.objects.get(name = category.sub_main_category.name)
        mainCategory = Main_Categories.objects.get(name = subCategory.main_categories.name)

        mainCategoryName = mainCategory.pk
        subCategoryName = subCategory.name

        allSubCategory = Sub_Main_Category.objects.filter(main_categories = mainCategory)
        allCategory = Category.objects.filter(sub_main_category = subCategory)

        allSubCategory = serializers.serialize('json', allSubCategory)
        allSubCategory = json.loads(allSubCategory)

        allCategory = serializers.serialize('json', allCategory)
        allCategory = json.loads(allCategory)

        email = request.session.get('email', False)
        supplier = Supplier.objects.get(email = email)
        business = Business.objects.get(supplier = supplier)
        product = Product.objects.filter(business = business).filter(code = request.POST['productCode'])

        response = {'mainCategoryName' : mainCategoryName,
        'subCategoryName' : subCategoryName,
        'allSubCategory' : allSubCategory,
        'allCategory' : allCategory,
        'description' : product[0].description,
        'additional' : product[0].additional_information,
        "spec1" : product[0].specification_1,
        "spec2" : product[0].specification_2,
        "spec3" : product[0].specification_3,
        "spec4" : product[0].specification_4,
        "spec5" : product[0].specification_5,
        "spec6" : product[0].specification_6,
        "spec7" : product[0].specification_7,
        "spec8" : product[0].specification_8,
        "spec9" : product[0].specification_9,
        "spec10" : product[0].specification_10,

        "desc1" : product[0].description_1,
        "desc2" : product[0].description_2,
        "desc3" : product[0].description_3,
        "desc4" : product[0].description_4,
        "desc5" : product[0].description_5,
        "desc6" : product[0].description_6,
        "desc7" : product[0].description_7,
        "desc8" : product[0].description_8,
        "desc9" : product[0].description_9,
        "desc10" : product[0].description_10,

        }
        return HttpResponse(json.dumps(response), content_type = 'application/json')

def logout(request):
    request.session.pop('email')
    return redirect('homepage:landingPage')

def getSupplierProfile(request, supplierId):
    print(supplierId)
    business = Business.objects.get(name = supplierId)
    products = Product.objects.filter(business = business)
    business.profile_views += 1
    business.save()
    print("Suppleir-----\n", business.supplier.full_name)
    context = {
        'business' : business,
        'products' : products,
    }
    return render(request, 'SupplierCustomerProfile.html', context)