from EDashboard import views

from django.urls import path
from django.conf.urls import url
urlpatterns = [
#Dashboard Section
    path('account/dashboard/',views.dashboard,name="dashboard"),
    #url(r'^account/dashboard/',views.dashboard,name="dashboard"),    
    
     path('account/dashboard/profiledetail/<str:pk>/',views.profileinfo,name="profileinfo"),
      #path('account/dashboard/profiledetail/<int:pk>/<str:slug>/',views.profileinfo,name="profileinfo"),
#Energy CRUD    
    path('account/dashboard/energy/',views.energy,name="energy"),
    path('account/dashboard/addenergy/',views.addenergy,name="addenergy"),
    path('account/dashboard/updateenergy/<str:pk>/update',views.updateenergy,name="updateenergy"),
    path('account/dashboard/energy/<str:pk>/delete/',views.deleteenergy,name="deleteenergy"),

#landscape CRUD    
    path('account/dashboard/landscape/',views.landscape,name="landscape"),
    path('account/dashboard/addlandscape/',views.addlandscape,name="addlandscape"),
    path('account/dashboard/updatelandscape/<str:pk>/update',views.updatelandscape,name="updatelandscape"),
    path('account/dashboard/landscape/<str:pk>/delete/',views.deletelandscape,name="deletelandscape"),

#character CRUD    
    path('account/dashboard/character/',views.character,name="character"),
    path('account/dashboard/addcharacter/',views.addcharacter,name="addcharacter"),
    path('account/dashboard/updatecharacter/<str:pk>/update',views.updatecharacter,name="updatecharacter"),
    path('account/dashboard/character/<str:pk>/delete/',views.deletecharacter,name="deletecharacter"),    

]
