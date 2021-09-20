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

from django.contrib.auth import views as auth_views

from EHub.urls import *
from VFX.urls import *
from SFX.urls import *
from OTHERS.urls import *
from SpecialPacks.urls import *
from GraphicsElements.urls import *
from EDashboard.urls import *
from EBlog.urls import *

from django.conf.urls import url# url mapping
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    
    url(r'^',include('EHub.urls')),#same as path('',include('EHub.urls')), 
    url(r'^',include('EBlog.urls')),
    path('',include('VFX.urls')), 
    path('',include('SFX.urls')), 
    path('',include('OTHERS.urls')),
    path('',include('GraphicsElements.urls')),   
    path('',include('SpecialPacks.urls')),      
    path('',include('EDashboard.urls')),          

    #Custom Url
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="PasswordReset/password_reset.html"),name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="PasswordReset/password_reset_sent.html"),name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="PasswordReset/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="PasswordReset/password_reset_done.html"), 
        name="password_reset_complete"),
]

from django.conf.urls.static import static
from django.conf import settings
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   # for acessing media url

     
'''
1 - Submit email form                         //PasswordResetView.as_view()
2 - Email sent success message                //PasswordResetDoneView.as_view()
3 - Link to password Rest form in email       //PasswordResetConfirmView.as_view()
4 - Password successfully changed message     //PasswordResetCompleteView.as_view()
'''