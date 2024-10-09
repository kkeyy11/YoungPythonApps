from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def coffee(request):
    context={}
    return render(request, "coffee/coffee.html", context )