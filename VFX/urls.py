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
from VFX import views
from .views import *
urlpatterns = [
    path('VFX/Energy/', views.energyvfx, name="EnergyVfx"),
    path('updateenergyvfx/', views.updateEnergyvfx, name="updateenergyvfx"),
        
    path('VFX/Lightinings/', views.electricityvfx, name="LightiningVfx"),
    path('updateelectricityvfx/', views.updatelightiningvfx, name="updateelectricityvfx"),     
    
    path('VFX/MuzzleFlashes/', views.muzzleflashes, name="MuzzleFlashesVfx"),
    path('updatemuzzleflashvfx/', views.updatemuzzleflashes, name="updatemuzzleflashvfx"),     
    
    path('VFX/Shockwaves/', views.shockwavesvfx, name="ShockwavesVfx"),
    path('updateshockwavevfx/', views.updateshockwavevfx, name="updateshockwavevfx"),     
    
    path('VFX/Particles/', views.particlesvfx, name="ParticlesVfx"),
    path('updateparticlevfx/', views.updateparticlevfx, name="updateparticlevfx"),     
    
    path('VFX/Environment/', views.environmentalvfx, name="EnvironmentVfx"),
    path('updateenvironmentalvfx/', views.updateenvironmentalvfx, name="updateenvironmentalvfx"),     

    path('VFX/DebrisAndCracks/', views.debrisandcracksvfx, name="DebrisAndCrackVfx"),
    path('updatedebrisandcrackvfx/', views.updatedebrisandcrackvfx, name="updatedebrisandcrackvfx"),     


]
