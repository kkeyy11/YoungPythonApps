from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('personalinfo/', views.personalinfo, name="personalinfo"),
    path('social/', views.social, name="social"),
    path('gameinfo/', views.gameinfo, name="gameinfo"),

]
   