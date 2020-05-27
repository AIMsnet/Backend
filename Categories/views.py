from django.shortcuts import render
from .models import Categories, Sub_Categories

# Create your views here.

def subCategory(request, subcategory):
    context = {
        "subCategory" : subcategory,
    }
    return render(request, "SubCategories.html", context)
