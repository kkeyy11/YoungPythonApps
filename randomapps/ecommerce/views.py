from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    return render(request, "ecommerce/index.html", context )
def shop(request):
    context={}
    return render(request, "ecommerce/shop.html", context )