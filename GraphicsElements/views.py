from django.shortcuts import render
from EHub.models import *
from GraphicsElements.models import *
from django.http import JsonResponse, response
import json                              # data = json.loads(request.body) 
import datetime

from django.contrib.auth import authenticate,login,logout  #For login and logout setup for registered users
from django.contrib.auth.decorators import login_required  #Restriciton ofp Pages (For not to display pages for anonymous user(but only logged in users))
from EHub.decorators import unauthenticated_user, allowed_users, admin_only 

def landscapes(request):
    if request.user.is_authenticated:
        getpaidlandscapes=Landscapes.objects.filter(type="PAID")  
        getfreelandscapes=Landscapes.objects.filter(type="FREE")     
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        TotalCartItems=order.get_lightiningvfx_items+order.get_energyvfx_items+order.get_muzzleflashes_items+order.get_shockwaves_items+order.get_particles_items+order.get_environmentvfx_items+order.get_debrisandcracksvfx_items+order.get_lightiningsfx_items+order.get_energysfx_items+order.get_environmentalsfx_items+order.get_firesfx_items+order.get_machinerysfx_items+order.get_weaponsfx_items+order.get_fightingsfx_items+order.get_landscapes_items+order.get_characters_items+order.get_opticallens_items+order.get_audiopack_items+order.get_vfxpack_items+order.get_flimtransitionpack_items+order.get_motiongraphicspack_items+order.get_audiospectrum_items+order.get_lyricstemplate_items
       
    else:
        getpaidlandscapes=Landscapes.objects.filter(type="PAID")  
        getfreelandscapes=Landscapes.objects.filter(type="FREE")    
        TotalCartItems=0
        
    context={ 
             'TotalCartItems':TotalCartItems,
             'getpaidlandscapes':getpaidlandscapes,
             'getfreelandscapes':getfreelandscapes,   
             }
    return render(request,'GraphicsElements/landscapes.html',context)  

def updatelandscape(request):
    print('Landscape(s) loaded to the API..')
    data = json.loads(request.body) # We are recieving  data(item was added) importing from json as a string and we need to parse it so for that we need .loads an we r sending back using request.body
    productName = data['productName'] 
    publisherId=data['publisherId']
    print(publisherId)
    action = data['action']
     #now we wanna print this out after parsing making them available in dictionary
    print('action:', action) 
    print('productName:', productName)  

    customer = request.user.customer #locking customer
    getlandscape=Landscapes.objects.get(name=productName)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    purchase, created = PurchasedProducts.objects.get_or_create(customer=customer, complete=False)      
    orderlandscape, created = OrderLandscape.objects.get_or_create(customer=customer,order=order, addtoDpage=purchase, published_by=publisherId,product=getlandscape,complete=False)
   
    #INCREASING OR DECREASING QUANTITY OF ORDER ITEM
    if action == 'add':
        if orderlandscape.quantity==0:
           orderlandscape.quantity = (orderlandscape.quantity + 1)
        elif orderlandscape.quantity==1:
           orderlandscape.quantity =orderlandscape.quantity 
    
    if action == 'remove':
        orderlandscape.quantity = (orderlandscape.quantity - 1)

    orderlandscape.save()

    if orderlandscape.quantity <=0: #if the orderitem is 0 delete it
        orderlandscape.delete()

    return JsonResponse('Item was added', safe=False)

def characters(request):
    if request.user.is_authenticated:
        getpaidcharacters=Characters.objects.filter(type="PAID")  
        getfreecharacters=Characters.objects.filter(type="FREE")     
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        TotalCartItems=order.get_lightiningvfx_items+order.get_energyvfx_items+order.get_muzzleflashes_items+order.get_shockwaves_items+order.get_particles_items+order.get_environmentvfx_items+order.get_debrisandcracksvfx_items+order.get_lightiningsfx_items+order.get_energysfx_items+order.get_environmentalsfx_items+order.get_firesfx_items+order.get_machinerysfx_items+order.get_weaponsfx_items+order.get_fightingsfx_items+order.get_landscapes_items+order.get_characters_items+order.get_opticallens_items+order.get_audiopack_items+order.get_vfxpack_items+order.get_flimtransitionpack_items+order.get_motiongraphicspack_items+order.get_audiospectrum_items+order.get_lyricstemplate_items
       
    else:
        getpaidcharacters=Characters.objects.filter(type="PAID")  
        getfreecharacters=Characters.objects.filter(type="FREE")    
        TotalCartItems=0
    context={ 
             'TotalCartItems':TotalCartItems,
             'getpaidcharacters':getpaidcharacters,
             'getfreecharacters':getfreecharacters,   
             }
    return render(request,'GraphicsElements/characters.html',context)  

def updatecharacters(request):
    print('Character(s) loaded to the API..')
    data = json.loads(request.body) # We are recieving  data(item was added) importing from json as a string and we need to parse it so for that we need .loads an we r sending back using request.body
    productName = data['productName'] 
    publisherId=data['publisherId']
    action = data['action']
     #now we wanna print this out after parsing making them available in dictionary
    print('action:', action) 
    print('productName:', productName)  

    customer = request.user.customer #locking customer
    getcharacter=Characters.objects.get(name=productName)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    purchase, created = PurchasedProducts.objects.get_or_create(customer=customer, complete=False)      
    ordercharacter, created = OrderCharacter.objects.get_or_create(customer=customer, order=order, addtoDpage=purchase, published_by=publisherId,product=getcharacter,complete=False)
   
    #INCREASING OR DECREASING QUANTITY OF ORDER ITEM
    if action == 'add':
        if ordercharacter.quantity==0:
           ordercharacter.quantity = (ordercharacter.quantity + 1)
        elif ordercharacter.quantity==1:
           ordercharacter.quantity =ordercharacter.quantity 
    
    if action == 'remove':
        ordercharacter.quantity = (ordercharacter.quantity - 1)

    ordercharacter.save()

    if ordercharacter.quantity <=0: #if the orderitem is 0 delete it
        ordercharacter.delete()

    return JsonResponse('Item was added', safe=False)

def opticallens(request):
    if request.user.is_authenticated:
        getpaidopticallens=OpticalLens.objects.filter(type="PAID")  
        getfreeopticallens=OpticalLens.objects.filter(type="FREE")     
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        TotalCartItems=order.get_lightiningvfx_items+order.get_energyvfx_items+order.get_muzzleflashes_items+order.get_shockwaves_items+order.get_particles_items+order.get_environmentvfx_items+order.get_debrisandcracksvfx_items+order.get_lightiningsfx_items+order.get_energysfx_items+order.get_environmentalsfx_items+order.get_firesfx_items+order.get_machinerysfx_items+order.get_weaponsfx_items+order.get_fightingsfx_items+order.get_landscapes_items+order.get_characters_items+order.get_opticallens_items+order.get_audiopack_items+order.get_vfxpack_items+order.get_flimtransitionpack_items+order.get_motiongraphicspack_items+order.get_audiospectrum_items+order.get_lyricstemplate_items
       
    else:
        getpaidopticallens=OpticalLens.objects.filter(type="PAID")  
        getfreeopticallens=OpticalLens.objects.filter(type="FREE")    
        TotalCartItems=0
    context={ 
             'TotalCartItems':TotalCartItems,
             'getpaidopticallens':getpaidopticallens,
             'getfreeopticallens':getfreeopticallens,   
             }
    return render(request,'GraphicsElements/opticallens.html',context)  

def updateopticallens(request):
    print('OpticalLens(s) loaded to the API..')
    data = json.loads(request.body) # We are recieving  data(item was added) importing from json as a string and we need to parse it so for that we need .loads an we r sending back using request.body
    productName = data['productName'] 
    publisherId=data['publisherId']
    action = data['action']
     #now we wanna print this out after parsing making them available in dictionary
    print('action:', action) 
    print('productName:', productName)  

    customer = request.user.customer #locking customer
    getopticallens=OpticalLens.objects.get(name=productName)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    purchase, created = PurchasedProducts.objects.get_or_create(customer=customer, complete=False)      
    orderopticallens, created = OrderOpticalLense.objects.get_or_create(customer=customer,order=order,  addtoDpage=purchase, published_by=publisherId,product=getopticallens,complete=False)
   
    #INCREASING OR DECREASING QUANTITY OF ORDER ITEM
    if action == 'add':
        if orderopticallens.quantity==0:
           orderopticallens.quantity = (orderopticallens.quantity + 1)
        elif orderopticallens.quantity==1:
           orderopticallens.quantity =orderopticallens.quantity 
    
    if action == 'remove':
        orderopticallens.quantity = (orderopticallens.quantity - 1)

    orderopticallens.save()

    if orderopticallens.quantity <=0: #if the orderitem is 0 delete it
        orderopticallens.delete()

    return JsonResponse('Item was added', safe=False)