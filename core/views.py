from django.shortcuts import render
from . models import Item

# Create your views here.

def list_item(request):
    context = {
        "items": Item.objects.all()
    }
    return render(request, "index.html", context)

def product_page(request):
    return render(request, "product_page.html")

def checkout_page(request):
    return render(request, "checkout.html")