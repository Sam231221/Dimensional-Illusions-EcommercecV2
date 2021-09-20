from django.shortcuts import render
from EHub.models import *
from SpecialPacks.models import *

from django.http import JsonResponse, response
import json      
import datetime
from django.contrib.auth.decorators import login_required  #Restriciton ofp Pages (For not to display pages for anonymous user(but only logged in users))
from EHub.decorators import unauthenticated_user, allowed_users, admin_only 

# Create your views here.

def soundpack(request):
    if request.user.is_authenticated:
        getpaidsoundpacks=SoundPack.objects.filter(type="PAID")  
        getfreesoundpacks=SoundPack.objects.filter(type="FREE")     
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        TotalCartItems=order.get_lightiningvfx_items+order.get_energyvfx_items+order.get_muzzleflashes_items+order.get_shockwaves_items+order.get_particles_items+order.get_environmentvfx_items+order.get_debrisandcracksvfx_items+order.get_lightiningsfx_items+order.get_energysfx_items+order.get_environmentalsfx_items+order.get_firesfx_items+order.get_machinerysfx_items+order.get_weaponsfx_items+order.get_fightingsfx_items+order.get_landscapes_items+order.get_characters_items+order.get_opticallens_items+order.get_audiopack_items+order.get_vfxpack_items+order.get_flimtransitionpack_items+order.get_motiongraphicspack_items+order.get_audiospectrum_items+order.get_lyricstemplate_items
       
    else:
        getpaidsoundpacks=SoundPack.objects.filter(type="PAID")  
        getfreesoundpacks=SoundPack.objects.filter(type="FREE")       
        TotalCartItems=0
    context={ 
             'TotalCartItems':TotalCartItems,             
             'getpaidsoundpacks':getpaidsoundpacks,
             'getfreesoundpacks':getfreesoundpacks,
             }    
    return render(request, 'SpecialPacks/SpecialSoundPacks.html',context)

def updatesoundpack(request):
    print('SoundPack(s) loaded to the API..')
    data = json.loads(request.body) # We are recieving  data(item was added) importing from json as a string and we need to parse it so for that we need .loads an we r sending back using request.body
    productName = data['productName'] 
    publisherId=data['publisherId']
    action = data['action']
     #now we wanna print this out after parsing making them available in dictionary
    print('action:', action) 
    print('productId:', productName)  

    customer = request.user.customer #locking customer
    product=SoundPack.objects.get(name=productName)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    purchase, created = PurchasedProducts.objects.get_or_create(customer=customer, complete=False)      
    ordersoundpack, created = OrderSoundPack.objects.get_or_create(published_by=publisherId,customer=customer, order=order, addtoDpage=purchase, product=product)
   #orderItem, created = OrderItem.objects.get_or_create(order=order, addtodpage=download, product=product)
    #INCREASING OR DECREASING QUANTITY OF ORDER ITEM
    if action == 'add':
        if ordersoundpack.quantity==0:
           ordersoundpack.quantity = (ordersoundpack.quantity + 1)
        elif ordersoundpack.quantity==1:
           ordersoundpack.quantity =ordersoundpack.quantity 
    
    if action == 'remove':
        ordersoundpack.quantity = (ordersoundpack.quantity - 1)

    ordersoundpack.save()

    if ordersoundpack.quantity <=0: #if the orderitem is 0 delete it
        ordersoundpack.delete()

    return JsonResponse('Item was added', safe=False)

def vfxpack(request):
    if request.user.is_authenticated:
        getpaidvfxpack=VfxPack.objects.filter(type="PAID")  
        getfreevfxpack=VfxPack.objects.filter(type="FREE")     
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        TotalCartItems=order.get_lightiningvfx_items+order.get_energyvfx_items+order.get_muzzleflashes_items+order.get_shockwaves_items+order.get_particles_items+order.get_environmentvfx_items+order.get_debrisandcracksvfx_items+order.get_lightiningsfx_items+order.get_energysfx_items+order.get_environmentalsfx_items+order.get_firesfx_items+order.get_machinerysfx_items+order.get_weaponsfx_items+order.get_fightingsfx_items+order.get_landscapes_items+order.get_characters_items+order.get_opticallens_items+order.get_audiopack_items+order.get_vfxpack_items+order.get_flimtransitionpack_items+order.get_motiongraphicspack_items+order.get_audiospectrum_items+order.get_lyricstemplate_items
       
    else:
        getpaidvfxpack=VfxPack.objects.filter(type="PAID")  
        getfreevfxpack=VfxPack.objects.filter(type="FREE")       
        TotalCartItems=0
    context={ 
             'TotalCartItems':TotalCartItems,             
             'getpaidvfxpack':getpaidvfxpack,
             'getfreevfxpack':getfreevfxpack,
             }    
    return render(request, 'SpecialPacks/SpecialVfxpack.html',context)

def updatevfxpack(request):
    print('VfxPack(s) loaded to the API..')
    data = json.loads(request.body) # We are recieving  data(item was added) importing from json as a string and we need to parse it so for that we need .loads an we r sending back using request.body
    productName = data['productName'] 
    publisherId=data['publisherId']
    action = data['action']
     #now we wanna print this out after parsing making them available in dictionary
    print('action:', action) 
    print('productId:', productName)  

    customer = request.user.customer #locking customer
    product=VfxPack.objects.get(name=productName)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    purchase, created = PurchasedProducts.objects.get_or_create(customer=customer, complete=False)      
    ordervfxpack, created = OrderVfxPack.objects.get_or_create(published_by=publisherId,customer=customer, order=order, addtoDpage=purchase, product=product)
 
    #INCREASING OR DECREASING QUANTITY OF ORDER ITEM
    if action == 'add':
        if ordervfxpack.quantity==0:
           ordervfxpack.quantity = (ordervfxpack.quantity + 1)
        elif ordervfxpack.quantity==1:
           ordervfxpack.quantity =ordervfxpack.quantity 
    
    if action == 'remove':
        ordervfxpack.quantity = (ordervfxpack.quantity - 1)

    ordervfxpack.save()

    if ordervfxpack.quantity <=0: #if the orderitem is 0 delete it
        ordervfxpack.delete()

    return JsonResponse('Item was added', safe=False)


def flimtransitionpack(request):
    if request.user.is_authenticated:
        getpaidflimtransitionpack=FlimTransitionPack.objects.filter(type="PAID")  
        getfreeflimtransitionpack=FlimTransitionPack.objects.filter(type="FREE")     
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        TotalCartItems=order.get_lightiningvfx_items+order.get_energyvfx_items+order.get_muzzleflashes_items+order.get_shockwaves_items+order.get_particles_items+order.get_environmentvfx_items+order.get_debrisandcracksvfx_items+order.get_lightiningsfx_items+order.get_energysfx_items+order.get_environmentalsfx_items+order.get_firesfx_items+order.get_machinerysfx_items+order.get_weaponsfx_items+order.get_fightingsfx_items+order.get_landscapes_items+order.get_characters_items+order.get_opticallens_items+order.get_audiopack_items+order.get_vfxpack_items+order.get_flimtransitionpack_items+order.get_motiongraphicspack_items+order.get_audiospectrum_items+order.get_lyricstemplate_items
       
    else:
        getpaidflimtransitionpack=FlimTransitionPack.objects.filter(type="PAID")  
        getfreeflimtransitionpack=FlimTransitionPack.objects.filter(type="FREE")       
        TotalCartItems=0
    context={ 
             'TotalCartItems':TotalCartItems,             
             'getpaidflimtransitionpack':getpaidflimtransitionpack,
             'getfreeflimtransitionpack':getfreeflimtransitionpack,
             }    
    return render(request, 'SpecialPacks/FlimTransitionPack.html',context)

def updateflimtransitionpack(request):
    print('FlimTransitionPack(s) loaded to the API..')
    data = json.loads(request.body) # We are recieving  data(item was added) importing from json as a string and we need to parse it so for that we need .loads an we r sending back using request.body
    productName = data['productName'] 
    publisherId=data['publisherId']
    action = data['action']
     #now we wanna print this out after parsing making them available in dictionary
    print('action:', action) 
    print('productId:', productName)  

    customer = request.user.customer #locking customer
    product=FlimTransitionPack.objects.get(name=productName)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    purchase, created = PurchasedProducts.objects.get_or_create(customer=customer, complete=False)      
    orderflimtransition, created = OrderFlimTransition.objects.get_or_create(published_by=publisherId,customer=customer, order=order, addtoDpage=purchase, product=product)
   #orderItem, created = OrderItem.objects.get_or_create(order=order, addtodpage=download, product=product)
    #INCREASING OR DECREASING QUANTITY OF ORDER ITEM
    if action == 'add':
        if orderflimtransition.quantity==0:
           orderflimtransition.quantity = (orderflimtransition.quantity + 1)
        elif orderflimtransition.quantity==1:
           orderflimtransition.quantity =orderflimtransition.quantity 
    
    if action == 'remove':
        orderflimtransition.quantity = (orderflimtransition.quantity - 1)

    orderflimtransition.save()

    if orderflimtransition.quantity <=0: #if the orderitem is 0 delete it
        orderflimtransition.delete()

    return JsonResponse('Item was added', safe=False)


def motiongraphicspack(request):
    if request.user.is_authenticated:
        getpaidmotiongraphicspack=MotionGraphicsPack.objects.filter(type="PAID")  
        getfreemotiongraphicspack=MotionGraphicsPack.objects.filter(type="FREE")     
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        TotalCartItems=order.get_lightiningvfx_items+order.get_energyvfx_items+order.get_muzzleflashes_items+order.get_shockwaves_items+order.get_particles_items+order.get_environmentvfx_items+order.get_debrisandcracksvfx_items+order.get_lightiningsfx_items+order.get_energysfx_items+order.get_environmentalsfx_items+order.get_firesfx_items+order.get_machinerysfx_items+order.get_weaponsfx_items+order.get_fightingsfx_items+order.get_landscapes_items+order.get_characters_items+order.get_opticallens_items+order.get_audiopack_items+order.get_vfxpack_items+order.get_flimtransitionpack_items+order.get_motiongraphicspack_items+order.get_audiospectrum_items+order.get_lyricstemplate_items
       
    else:
        getpaidmotiongraphicspack=MotionGraphicsPack.objects.filter(type="PAID")  
        getfreemotiongraphicspack=MotionGraphicsPack.objects.filter(type="FREE")       
        TotalCartItems=0
    context={ 
             'TotalCartItems':TotalCartItems,             
             'getpaidmotiongraphicspack':getpaidmotiongraphicspack,
             'getfreemotiongraphicspack':getfreemotiongraphicspack,
             }    
    return render(request, 'SpecialPacks/MotionGraphicsPack.html',context)

def updatemotiongraphicspack(request):
    print('MotionGraphicsPack(s) loaded to the API..')
    data = json.loads(request.body) # We are recieving  data(item was added) importing from json as a string and we need to parse it so for that we need .loads an we r sending back using request.body
    productName = data['productName'] 
    publisherId=data['publisherId']
    action = data['action']
     #now we wanna print this out after parsing making them available in dictionary
    print('action:', action) 
    print('productId:', productName)  

    customer = request.user.customer #locking customer
    product=MotionGraphicsPack.objects.get(name=productName)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    purchase, created = PurchasedProducts.objects.get_or_create(customer=customer, complete=False)      
    ordermotiongraphicspack, created = OrderMotionGraphicsPack.objects.get_or_create(published_by=publisherId,customer=customer, order=order, addtoDpage=purchase, product=product)
  
    #INCREASING OR DECREASING QUANTITY OF ORDER ITEM
    if action == 'add':
        if ordermotiongraphicspack.quantity==0:
           ordermotiongraphicspack.quantity = (ordermotiongraphicspack.quantity + 1)
        elif ordermotiongraphicspack.quantity==1:
           ordermotiongraphicspack.quantity =ordermotiongraphicspack.quantity 
    
    if action == 'remove':
        ordermotiongraphicspack.quantity = (ordermotiongraphicspack.quantity - 1)

    ordermotiongraphicspack.save()

    if ordermotiongraphicspack.quantity <=0: #if the orderitem is 0 delete it
        ordermotiongraphicspack.delete()

    return JsonResponse('Item was added', safe=False)


