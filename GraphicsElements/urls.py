"""
Dimensionalillusions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    
"""
from django.contrib import admin
from django.urls import path
from GraphicsElements import views
from .views import *
urlpatterns = [
    path('GraphicsElements/Landscapes', views.landscapes, name="Landscapes"),
    path('UpdateLandscape/', views.updatelandscape, name="UpdateLandscape"),    
    
    path('GraphicsElements/Characters', views.characters, name="Characters"),
    path('UpdateCharacter/', views.updatecharacters, name="UpdateCharacter"),   
    
    path('GraphicsElements/Opticallens', views.opticallens, name="Opticallens"),
    path('UpdateOpticallens/', views.updateopticallens, name="UpdateOpticallens"),   
]
