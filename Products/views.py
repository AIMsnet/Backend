from django.shortcuts import render, HttpResponse
from Supplier.models import Product, Quote
from Customer.models import Customer
from django.core import serializers
import json
# Pagination
from django.core.paginator import Paginator

def product(request, productName):
    product = Product.objects.filter(name__contains = productName)
    paginator = Paginator(product, 5)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        product = paginator.page(page)
    except(EmptyPage, InvalidPage):
        product = paginator.page(paginator.num_pages)

    customer = request.session.get('customer', False)
    if(customer == False):
        log = False
    else:
        log = True

    return render(request, "ProductDisplay.html", {'product' : product, 'log' : log})

def getProduct(request):
    if request.method == "POST":
        customer = request.session.get('customer', False)
        if(customer != False):
            productId = request.POST['productId']
            productQty = request.POST['productQty']
            productReq = request.POST['productRequirements']
            customer = Customer.objects.get(mobile_number = customer)
            product = Product.objects.get(pk = productId)
            Quote.objects.create(quantity = productQty, 
            requirement = productReq,
            product = product,
            customer = customer,
            supplier = product.business.supplier
            )
            response = {'status': 0, "message" : "Quote Submitted"}
            return HttpResponse(json.dumps(response), content_type='application/json')
        else:
            response = {'status': 1}
            return HttpResponse(json.dumps(response), content_type='application/json')
    else:
        print("Inside get Product----------------------------")
        product = Product.objects.get(pk = request.GET['pk'])
        product = serializers.serialize('json', [product])
        product = json.loads(product)
        response = {'status': 0, "product" : product}
        return HttpResponse(json.dumps(response), content_type='application/json')

def productDescription(request, pk):
    product = Product.objects.get(pk = pk)
    product.clicks += 1
    product.save() 
    customer = request.session.get('customer', False)
    if(customer == False):
        log = False
    else:
        log = True
    return render(request, "ProductDescription.html", {"product" : product, "log" : log})

