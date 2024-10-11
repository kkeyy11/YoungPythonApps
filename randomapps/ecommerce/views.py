from django.shortcuts import render

# Create your views here.

def index(request):
    
    return render(request, "ecommerce/index.html")
def shop(request):
   
    return render(request, "ecommerce/shop.html")
def contact(request):
    
    return render(request, "ecommerce/contact.html")