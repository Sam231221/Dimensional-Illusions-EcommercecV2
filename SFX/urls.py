"""Dimensionalillusions URL Configuration

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
from SFX import views
from .views import *
urlpatterns = [
    path('SFX/Fire/', views.firesfx, name="Firesfx"),
    path('updatefiresfx/', views.updatefiresfx, name="updatefiresfx"),      
    
    path('SFX/Energy/', views.energysfx, name="EnergySfx"),   
    path('updateEnergysfx/', views.updateEnergysfx, name="updateEnergysfx"),
    
    path('SFX/Lightinings/', views.electricitysfx, name="LightiningSfx"),
    path('updatelightiningsfx/', views.updatelightiningsfx, name="updatelightiningsfx"),
    
    path('SFX/Environment/', views.environmentalsfx, name="EnvironmentSfx"),
    path('updateEnvironmentalsfx/', views.updateenvironmentalsfx, name="updateEnvironmentalsfx"),
    
    path('SFX/Machinery/', views.machinerysfx, name="MachinerySfx"),   
    path('updatemachinerysfx/', views.updatemachinerysfx, name="updatemachinerysfx"),
   
    path('SFX/Weapons/', views.weaponsfx, name="WeaponSfx"),
    path('updateweaponsfx/', views.updateweaponsfx, name="updateWeaponsfx"),
    
    path('SFX/Fighting/', views.fightingsfx, name="FightingSfx"),   
    path('updatefightingsfx/', views.updatefightingsfx, name="updateFightingsfx"),
        
]
