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
from EHub import views
from .views import *
urlpatterns = [
    path('', views.Home, name="home"),

    #Authetication 
    path('account/register/' , register , name="register"),
    path('account/login/' , loginuser, name="login"),
    path('account/logout/',views.logoutUser, name="logout"),
    path('account/token/' , token_send , name="token_send"),
    path('account/success/' , success , name='success'),
    path('account/verify/<auth_token>' , verify , name="verify"),
    path('account/error/' , error_page , name="error"),

    path('search/', views.SearchEngine, name="search"),
    path('Contact_Us/', views.ContactApi, name="Contact_Us"),
    
    path('downloadpage/', views.DownloadProducts, name="download"),

    path('YourCart/', views.YourCart, name="YourCart"),
    path('Checkout/', views.Checkout, name="Checkout"),
    path("khalti-verify/", KhaltiVerifyView.as_view(), name="khaltiverify"),    
    
    path('process_order/', views.ProcessOrder, name="process_order"),    
        


]

