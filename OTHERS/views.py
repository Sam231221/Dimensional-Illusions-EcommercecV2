from django.shortcuts import render
from OTHERS.models import  *
from django.http import JsonResponse, response
import json                              # data = json.loads(request.body) 
import datetime

from django.contrib.auth import authenticate,login,logout  #For login and logout setup for registered users

from django.contrib.auth.decorators import login_required  #Restriciton ofp Pages (For not to display pages for anonymous user(but only logged in users))

from EHub.decorators import unauthenticated_user, allowed_users, admin_only  #Maintaining privacy(pages that are restricted and allowed to common users )

# Create your views here.
#TEMPLATES SECTION 
def audiospectrums(request):
    if request.user.is_authenticated:
        getpaidaudiospectrums=AudioSpectrum.objects.filter(type="PAID")  
        getfreeaudiospectrums=AudioSpectrum.objects.filter(type="FREE")     
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        TotalCartItems=order.get_lightiningvfx_items+order.get_energyvfx_items+order.get_muzzleflashes_items+order.get_shockwaves_items+order.get_particles_items+order.get_environmentvfx_items+order.get_debrisandcracksvfx_items+order.get_lightiningsfx_items+order.get_energysfx_items+order.get_environmentalsfx_items+order.get_firesfx_items+order.get_machinerysfx_items+order.get_weaponsfx_items+order.get_fightingsfx_items+order.get_landscapes_items+order.get_characters_items+order.get_opticallens_items+order.get_audiopack_items+order.get_vfxpack_items+order.get_flimtransitionpack_items+order.get_motiongraphicspack_items+order.get_audiospectrum_items+order.get_lyricstemplate_items
       
    else:
        getpaidaudiospectrums=AudioSpectrum.objects.filter(type="PAID")  
        getfreeaudiospectrums=AudioSpectrum.objects.filter(type="FREE")    
        TotalCartItems=0
    context={ 
             'TotalCartItems':TotalCartItems,
             'getpaidaudiospectrums':getpaidaudiospectrums,
             'getfreeaudiospectrums':getfreeaudiospectrums,   
             }
    return render(request,'AE-Templates/Audiospectrum.html',context)  

def updatespectrum(request):
    print('AudioSpectrum(s) loaded to the API..')
    data = json.loads(request.body) # We are recieving  data(item was added) importing from json as a string and we need to parse it so for that we need .loads an we r sending back using request.body
    productName = data['productName'] 
    publisherId=data['publisherId']
    action = data['action']
     #now we wanna print this out after parsing making them available in dictionary
    print('action:', action) 
    print('productName:', productName)  

    customer = request.user.customer #locking customer
    getspectrum=AudioSpectrum.objects.get(name=productName)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    purchase, created = PurchasedProducts.objects.get_or_create(customer=customer, complete=False)      
    orderspectrum, created = OrderAudioSpectrum.objects.get_or_create( publisher_Id=publisherId,order=order, addtoDpage=purchase, product=getspectrum,complete=False)
   
    #INCREASING OR DECREASING QUANTITY OF ORDER ITEM
    if action == 'add':
        if orderspectrum.quantity==0:
           orderspectrum.quantity = (orderspectrum.quantity + 1)
        elif orderspectrum.quantity==1:
           orderspectrum.quantity =orderspectrum.quantity 
    
    if action == 'remove':
        orderspectrum.quantity = (orderspectrum.quantity - 1)

    orderspectrum.save()

    if orderspectrum.quantity <=0: #if the orderitem is 0 delete it
        orderspectrum.delete()

    return JsonResponse('Item was added', safe=False)

def lyricstemplates(request):
    if request.user.is_authenticated:
        getpaidlyricstemplates=LyricsTemplate.objects.filter(type="PAID")  
        getfreelyricstemplates=LyricsTemplate.objects.filter(type="FREE")     
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        TotalCartItems=order.get_lightiningvfx_items+order.get_energyvfx_items+order.get_muzzleflashes_items+order.get_shockwaves_items+order.get_particles_items+order.get_environmentvfx_items+order.get_debrisandcracksvfx_items+order.get_lightiningsfx_items+order.get_energysfx_items+order.get_environmentalsfx_items+order.get_firesfx_items+order.get_machinerysfx_items+order.get_weaponsfx_items+order.get_fightingsfx_items+order.get_landscapes_items+order.get_characters_items+order.get_opticallens_items+order.get_audiopack_items+order.get_vfxpack_items+order.get_flimtransitionpack_items+order.get_motiongraphicspack_items+order.get_audiospectrum_items+order.get_lyricstemplate_items
       
    else:
        getpaidlyricstemplates=LyricsTemplate.objects.filter(type="PAID")  
        getfreelyricstemplates=LyricsTemplate.objects.filter(type="FREE")    
        TotalCartItems=0
    context={ 
             'TotalCartItems':TotalCartItems,
             'getpaidlyricstemplates':getpaidlyricstemplates,
             'getfreelyricstemplates':getfreelyricstemplates, 
             }
    return render(request,'AE-Templates/Lyricstemplates.html',context)  

def updatelyricstemplate(request):
    print('Lyrics template(s) loaded to the API..')
    data = json.loads(request.body) # We are recieving  data(item was added) importing from json as a string and we need to parse it so for that we need .loads an we r sending back using request.body
    productName = data['productName'] 
    publisherId=data['publisherId']
    action = data['action']
     #now we wanna print this out after parsing making them available in dictionary
    print('action:', action) 
    print('productName:', productName)  

    customer = request.user.customer #locking customer
    getlyricstemplate=LyricsTemplate.objects.get(name=productName)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    purchase, created = PurchasedProducts.objects.get_or_create(customer=customer, complete=False)      
    orderlyricstemplate, created = OrderLyricsTemplates.objects.get_or_create( publisher_Id=publisherId,order=order, addtoDpage=purchase, product=getlyricstemplate,complete=False)
   
    #INCREASING OR DECREASING QUANTITY OF ORDER ITEM
    if action == 'add':
        if orderlyricstemplate.quantity==0:
           orderlyricstemplate.quantity = (orderlyricstemplate.quantity + 1)
        elif orderlyricstemplate.quantity==1:
           orderlyricstemplate.quantity =orderlyricstemplate.quantity 
    
    if action == 'remove':
        orderlyricstemplate.quantity = (orderlyricstemplate.quantity - 1)

    orderlyricstemplate.save()

    if orderlyricstemplate.quantity <=0: #if the orderitem is 0 delete it
        orderlyricstemplate.delete()

    return JsonResponse('Item was added', safe=False)
