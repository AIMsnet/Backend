from django.shortcuts import render, HttpResponse, redirect
from django.core import serializers
import json
from Supplier.models import Main_Categories, Sub_Main_Category, Category

# Create your views here.

def subCategory(request, subcategory):
    mainCategory = Main_Categories.objects.get(name = subcategory)
    subCategoryList = Sub_Main_Category.objects.filter(main_categories = mainCategory)
    print("Got it", subCategoryList[0])
    context = {
        "subCategory" : subCategoryList,
        "category" : subcategory
    }    
    return render(request, "SubCategories.html", context)


def getCategories(request):
    if request.method == 'POST':
        id = request.POST['subCatId']
        subCategory = Sub_Main_Category.objects.get(pk = id)
        category = Category.objects.filter(sub_main_category = subCategory)
        category = serializers.serialize('json', category)
        category = json.loads(category)
        response = {'status' : 0, 'category' : category}

        return HttpResponse(json.dumps(response), content_type='application/json')