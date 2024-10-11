from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request, "portfolio/home.html")
def gameinfo(request):
 
    return render(request, "portfolio/gameinfo.html" )
def personalinfo(request):
  
    return render(request, "portfolio/personalinfo.html" )
def social(request):

    return render(request, "portfolio/social.html")