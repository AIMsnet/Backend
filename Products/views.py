from django.shortcuts import render

# Create your views here.

def product(request, *args, **kwargs):
    return render(request, "ProductDisplay.html")

def productDescription(request):
    print("kha;shflashfbkjashfjkabsfl;hasd;fh")
    return render(request, "ProductDescription.html")