from django.shortcuts import render

# Create your views here.

def home(request):
    context={}
    return render(request, "portfolio/home.html", context )
def gameinfo(request):
    context={}
    return render(request, "portfolio/gameinfo.html", context )
def personalinfo(request):
    context={}
    return render(request, "portfolio/personalinfo.html", context )
def social(request):
    context={}
    return render(request, "portfolio/social.html", context )