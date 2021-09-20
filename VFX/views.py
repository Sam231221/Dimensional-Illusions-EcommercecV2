from django.shortcuts import render
from EHub.models import *
from VFX.models import *

from django.http import JsonResponse, response
import json                              # data = json.loads(request.body) 
import datetime

from django.contrib.auth.decorators import login_required  #Restriciton ofp Pages (For not to display pages for anonymous user(but only logged in users))
from .decorators import unauthenticated_user, allowed_users, admin_only 

# Create your views here.
#VFX SECTION   
def electricityvfx(request):
    if request.user.is_authenticated:
        getpaidlightiningvfx=LightiningVfx.objects.filter(type="PAID")  
        getfreelightiningvfx=LightiningVfx.objects.filter(type="FREE")     
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        TotalCartItems=order.get_lightiningvfx_items+order.get_energyvfx_items+order.get_muzzleflashes_items+order.get_shockwaves_items+order.get_particles_items+order.get_environmentvfx_items+order.get_debrisandcracksvfx_items+order.get_lightiningsfx_items+order.get_energysfx_items+order.get_environmentalsfx_items+order.get_firesfx_items+order.get_machinerysfx_items+order.get_weaponsfx_items+order.get_fightingsfx_items+order.get_landscapes_items+order.get_characters_items+order.get_opticallens_items+order.get_audiopack_items+order.get_vfxpack_items+order.get_flimtransitionpack_items+order.get_motiongraphicspack_items+order.get_audiospectrum_items+order.get_lyricstemplate_items
       
    else:
        getpaidlightiningvfx=LightiningVfx.objects.filter(type="PAID")  
        getfreelightiningvfx=LightiningVfx.objects.filter(type="FREE")      
        TotalCartItems=0
         
    context={ 
             'TotalCartItems':TotalCartItems,
             'getpaidlightiningvfx':getpaidlightiningvfx,
             'getfreelightiningvfx':getfreelightiningvfx,   
             }
    return render(request, 'VFX/Electricity.html',context)

def updatelightiningvfx(request):
    print('LightiningVfx(s) loaded to the API..')
    data = json.loads(request.body) # We are recieving  data(item was added) importing from json as a string and we need to parse it so for that we need .loads an we r sending back using request.body
    productName = data['productName'] 
    publisherId=data['publisherId']
    action = data['action']
    print('action:', action) 
    print('productName:', productName)  

    customer = request.user.customer #locking customer
    getlightiningvfx=LightiningVfx.objects.get(name=productName)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    purchase, created = PurchasedProducts.objects.get_or_create(customer=customer, complete=False)    
    orderlightiningvfx, created = OrderLightiningVfx.objects.get_or_create(customer=customer, order=order, addtoDpage=purchase, product=getlightiningvfx,published_by=publisherId,complete=False)
  
    #INCREASING OR DECREASING QUANTITY OF ORDER ITEM
    if action == 'add':
        if orderlightiningvfx.quantity==0:
           orderlightiningvfx.quantity = (orderlightiningvfx.quantity + 1)
        elif orderlightiningvfx.quantity==1:
           orderlightiningvfx.quantity =orderlightiningvfx.quantity 
    
    if action == 'remove':
        orderlightiningvfx.quantity = (orderlightiningvfx.quantity - 1)

    orderlightiningvfx.save()

    if orderlightiningvfx.quantity <=0: 
        orderlightiningvfx.delete()

    return JsonResponse('Item was added', safe=False)

def energyvfx(request):
    if request.user.is_authenticated:
        getpaidEnergyvfx=EnergyVfx.objects.filter(type="PAID")  
        getfreeEnergyvfx=EnergyVfx.objects.filter(type="FREE")     
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        TotalCartItems=order.get_lightiningvfx_items+order.get_energyvfx_items+order.get_muzzleflashes_items+order.get_shockwaves_items+order.get_particles_items+order.get_environmentvfx_items+order.get_debrisandcracksvfx_items+order.get_lightiningsfx_items+order.get_energysfx_items+order.get_environmentalsfx_items+order.get_firesfx_items+order.get_machinerysfx_items+order.get_weaponsfx_items+order.get_fightingsfx_items+order.get_landscapes_items+order.get_characters_items+order.get_opticallens_items+order.get_audiopack_items+order.get_vfxpack_items+order.get_flimtransitionpack_items+order.get_motiongraphicspack_items+order.get_audiospectrum_items+order.get_lyricstemplate_items
       
    else:
        TotalCartItems=0
        getpaidEnergyvfx=EnergyVfx.objects.filter(type="PAID")  
        getfreeEnergyvfx=EnergyVfx.objects.filter(type="FREE")       

    context={ 
             'TotalCartItems':TotalCartItems,
             'getpaidEnergyvfx':getpaidEnergyvfx,
             'getfreeEnergyvfx':getfreeEnergyvfx,   
             }
    return render(request,'VFX/Energy.html',context) 
   
def updateEnergyvfx(request):
    print('EnergyVfx(s) loaded to the API..')
    data = json.loads(request.body) 
    productName = data['productName'] 
    publisherId=data['publisherId']
    action = data['action']
    print('action:', action) 

    print('productName:', productName)  
    customer = request.user.customer #locking customer
    getEnergyvfx=EnergyVfx.objects.get(name=productName)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    purchase, created = PurchasedProducts.objects.get_or_create(customer=customer, complete=False)    
    orderEnergyvfx, created = OrderEnergyVfx.objects.get_or_create(customer=customer, order=order, addtoDpage=purchase,published_by=publisherId, product=getEnergyvfx,complete=False)
   
    #INCREASING OR DECREASING QUANTITY OF ORDER ITEM
    if action == 'add':
        if orderEnergyvfx.quantity==0:
           orderEnergyvfx.quantity = (orderEnergyvfx.quantity + 1)
        elif orderEnergyvfx.quantity==1:
           orderEnergyvfx.quantity =orderEnergyvfx.quantity 
    
    if action == 'remove':
        orderEnergyvfx.quantity = (orderEnergyvfx.quantity - 1)

    orderEnergyvfx.save()

    if orderEnergyvfx.quantity <=0: #if the orderitem is 0 delete it
        orderEnergyvfx.delete()

    return JsonResponse('Item was added', safe=False)

def muzzleflashes(request):
    if request.user.is_authenticated:
        getpaidMuzzleflashes=MuzzleFlahses.objects.filter(type="PAID")  
        getfreeMuzzleflashes=MuzzleFlahses.objects.filter(type="FREE")     
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        TotalCartItems=order.get_lightiningvfx_items+order.get_energyvfx_items+order.get_muzzleflashes_items+order.get_shockwaves_items+order.get_particles_items+order.get_environmentvfx_items+order.get_debrisandcracksvfx_items+order.get_lightiningsfx_items+order.get_energysfx_items+order.get_environmentalsfx_items+order.get_firesfx_items+order.get_machinerysfx_items+order.get_weaponsfx_items+order.get_fightingsfx_items+order.get_landscapes_items+order.get_characters_items+order.get_opticallens_items+order.get_audiopack_items+order.get_vfxpack_items+order.get_flimtransitionpack_items+order.get_motiongraphicspack_items+order.get_audiospectrum_items+order.get_lyricstemplate_items
       
    else:
        getpaidMuzzleflashes=MuzzleFlahses.objects.filter(type="PAID")  
        getfreeMuzzleflashes=MuzzleFlahses.objects.filter(type="FREE")     
        TotalCartItems=0  

    context={ 
             'TotalCartItems':TotalCartItems,
             'getpaidMuzzleflashes':getpaidMuzzleflashes,
             'getfreeMuzzleflashes':getfreeMuzzleflashes,   
             }
    return render(request,'VFX/MuzzleFlashes.html',context) 
   
def updatemuzzleflashes(request):
    print('Muzzlefashe(s) loaded to the API..')
    data = json.loads(request.body) 
    productName = data['productName'] 
    publisherId=data['publisherId']
    action = data['action']
    print('action:', action) 
    print('productName:', productName)  
    customer = request.user.customer #locking customer
    getmuzzleflashes=MuzzleFlahses.objects.get(name=productName)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    purchase, created = PurchasedProducts.objects.get_or_create(customer=customer, complete=False)    
    orderMuzzleflashes, created = OrderMuzzleflashesVfx.objects.get_or_create(customer=customer, order=order, addtoDpage=purchase,published_by=publisherId, product=getmuzzleflashes,complete=False)
   
    #INCREASING OR DECREASING QUANTITY OF ORDER ITEM
    if action == 'add':
        if orderMuzzleflashes.quantity==0:
           orderMuzzleflashes.quantity = (orderMuzzleflashes.quantity + 1)
        elif orderMuzzleflashes.quantity==1:
           orderMuzzleflashes.quantity =orderMuzzleflashes.quantity 
    
    if action == 'remove':
        orderMuzzleflashes.quantity = (orderMuzzleflashes.quantity - 1)

    orderMuzzleflashes.save()

    if orderMuzzleflashes.quantity <=0: #if the orderitem is 0 delete it
        orderMuzzleflashes.delete()

    return JsonResponse('Item was added', safe=False)

def shockwavesvfx(request):
    if request.user.is_authenticated:
        getpaidshockwaves=ShockwavesVfx.objects.filter(type="PAID")  
        getfreeshockwaves=ShockwavesVfx.objects.filter(type="FREE")     
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        TotalCartItems=order.get_lightiningvfx_items+order.get_energyvfx_items+order.get_muzzleflashes_items+order.get_shockwaves_items+order.get_particles_items+order.get_environmentvfx_items+order.get_debrisandcracksvfx_items+order.get_lightiningsfx_items+order.get_energysfx_items+order.get_environmentalsfx_items+order.get_firesfx_items+order.get_machinerysfx_items+order.get_weaponsfx_items+order.get_fightingsfx_items+order.get_landscapes_items+order.get_characters_items+order.get_opticallens_items+order.get_audiopack_items+order.get_vfxpack_items+order.get_flimtransitionpack_items+order.get_motiongraphicspack_items+order.get_audiospectrum_items+order.get_lyricstemplate_items
       
    else:
        TotalCartItems=0
        getpaidshockwaves=ShockwavesVfx.objects.filter(type="PAID")  
        getfreeshockwaves=ShockwavesVfx.objects.filter(type="FREE")       

    context={ 
             'TotalCartItems':TotalCartItems,
             'getpaidshockwaves':getpaidshockwaves,
             'getfreeshockwaves':getfreeshockwaves,   
             }
    return render(request,'VFX/Shockwaves.html',context) 
   
def updateshockwavevfx(request):
    print('ShockwaveVfx(s) loaded to the API..')
    data = json.loads(request.body) 
    productName = data['productName'] 
    publisherId=data['publisherId']
    action = data['action']
    print('action:', action) 
    print('productName:', productName)  
    customer = request.user.customer #locking customer
    product=ShockwavesVfx.objects.get(name=productName)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    purchase, created = PurchasedProducts.objects.get_or_create(customer=customer, complete=False)    
    orderShockwavevfx, created = OrderShockwavesVfx.objects.get_or_create(customer=customer, order=order, addtoDpage=purchase,published_by=publisherId, product=product,complete=False)
   

    if action == 'add':
        if orderShockwavevfx.quantity==0:
           orderShockwavevfx.quantity = (orderShockwavevfx.quantity + 1)
        elif orderShockwavevfx.quantity==1:
           orderShockwavevfx.quantity =orderShockwavevfx.quantity 
    
    if action == 'remove':
        orderShockwavevfx.quantity = (orderShockwavevfx.quantity - 1)

    orderShockwavevfx.save()

    if orderShockwavevfx.quantity <=0: #if the orderitem is 0 delete it
        orderShockwavevfx.delete()

    return JsonResponse('Item was added', safe=False)

def particlesvfx(request):
    if request.user.is_authenticated:
        getpaidparticlesvfx=ParticlesVfx.objects.filter(type="PAID")  
        getfreeparticlesvfx=ParticlesVfx.objects.filter(type="FREE")     
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        TotalCartItems=order.get_lightiningvfx_items+order.get_energyvfx_items+order.get_muzzleflashes_items+order.get_shockwaves_items+order.get_particles_items+order.get_environmentvfx_items+order.get_debrisandcracksvfx_items+order.get_lightiningsfx_items+order.get_energysfx_items+order.get_environmentalsfx_items+order.get_firesfx_items+order.get_machinerysfx_items+order.get_weaponsfx_items+order.get_fightingsfx_items+order.get_landscapes_items+order.get_characters_items+order.get_opticallens_items+order.get_audiopack_items+order.get_vfxpack_items+order.get_flimtransitionpack_items+order.get_motiongraphicspack_items+order.get_audiospectrum_items+order.get_lyricstemplate_items
       
    else:
        TotalCartItems=0
        getpaidparticlesvfx=ParticlesVfx.objects.filter(type="PAID")  
        getfreeparticlesvfx=ParticlesVfx.objects.filter(type="FREE")       

    context={ 
             'TotalCartItems':TotalCartItems,
             'getpaidparticlesvfx':getpaidparticlesvfx,
             'getfreeparticlesvfx':getfreeparticlesvfx,   
             }
    return render(request,'VFX/Particles.html',context) 
   
def updateparticlevfx(request):
    print('ParticleVfx(s) loaded to the API..')
    data = json.loads(request.body) 
    productName = data['productName']
    publisherId=data['publisherId'] 
    action = data['action']
    print('action:', action) 
    print('productName:', productName)  
    customer = request.user.customer #locking customer
    product=ParticlesVfx.objects.get(name=productName)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    purchase, created = PurchasedProducts.objects.get_or_create(customer=customer, complete=False)    
    orderParticlevfx, created = OrderParticleVfx.objects.get_or_create(customer=customer, order=order, addtoDpage=purchase,published_by=publisherId, product=product,complete=False)
   
    if action == 'add':
        if orderParticlevfx.quantity==0:
           orderParticlevfx.quantity = (orderParticlevfx.quantity + 1)
        elif orderParticlevfx.quantity==1:
           orderParticlevfx.quantity =orderParticlevfx.quantity 
    
    if action == 'remove':
        orderParticlevfx.quantity = (orderParticlevfx.quantity - 1)

    orderParticlevfx.save()

    if orderParticlevfx.quantity <=0: #if the orderitem is 0 delete it
        orderParticlevfx.delete()

    return JsonResponse('Item was added', safe=False)

def environmentalvfx(request):
    if request.user.is_authenticated:
        getpaidenvironmentalvfx=EnvironmentalVfx.objects.filter(type="PAID")  
        getfreeenvironmentalvfx=EnvironmentalVfx.objects.filter(type="FREE")     
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        TotalCartItems=order.get_lightiningvfx_items+order.get_energyvfx_items+order.get_muzzleflashes_items+order.get_shockwaves_items+order.get_particles_items+order.get_environmentvfx_items+order.get_debrisandcracksvfx_items+order.get_lightiningsfx_items+order.get_energysfx_items+order.get_environmentalsfx_items+order.get_firesfx_items+order.get_machinerysfx_items+order.get_weaponsfx_items+order.get_fightingsfx_items+order.get_landscapes_items+order.get_characters_items+order.get_opticallens_items+order.get_audiopack_items+order.get_vfxpack_items+order.get_flimtransitionpack_items+order.get_motiongraphicspack_items+order.get_audiospectrum_items+order.get_lyricstemplate_items
       
    else:
        TotalCartItems=0
        getpaidenvironmentalvfx=EnvironmentalVfx.objects.filter(type="PAID")  
        getfreeenvironmentalvfx=EnvironmentalVfx.objects.filter(type="FREE")       

    context={ 
             'TotalCartItems':TotalCartItems,
             'getpaidenvironmentalvfx':getpaidenvironmentalvfx,
             'getfreeenvironmentalvfx':getfreeenvironmentalvfx,   
             }
    return render(request,'VFX/Environment.html',context) 

def updateenvironmentalvfx(request):
    print('EnvironmentalVfx(s) loaded to the API..')
    data = json.loads(request.body) 
    productName = data['productName'] 
    publisherId=data['publisherId']
    action = data['action']
    print('action:', action) 
    print('productName:', productName)  
    customer = request.user.customer #locking customer
    product=EnvironmentalVfx.objects.get(name=productName)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    purchase, created = PurchasedProducts.objects.get_or_create(customer=customer, complete=False)    
    orderEnvironmentalvfx, created = OrderEnvironmentalVfx.objects.get_or_create(customer=customer, order=order, addtoDpage=purchase,published_by=publisherId, product=product,complete=False)
   

    if action == 'add':
        if orderEnvironmentalvfx.quantity==0:
           orderEnvironmentalvfx.quantity = (orderEnvironmentalvfx.quantity + 1)
        elif orderEnvironmentalvfx.quantity==1:
           orderEnvironmentalvfx.quantity =orderEnvironmentalvfx.quantity 
    
    if action == 'remove':
        orderEnvironmentalvfx.quantity = (orderEnvironmentalvfx.quantity - 1)

    orderEnvironmentalvfx.save()

    if orderEnvironmentalvfx.quantity <=0: #if the orderitem is 0 delete it
        orderEnvironmentalvfx.delete()

    return JsonResponse('Item was added', safe=False)

def debrisandcracksvfx(request):
    if request.user.is_authenticated:
        getpaiddebrisandcrackvfx=DebrisandCracksVfx.objects.filter(type="PAID")  
        getfreedebrisandcrackvfx=DebrisandCracksVfx.objects.filter(type="FREE")     
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        TotalCartItems=order.get_lightiningvfx_items+order.get_energyvfx_items+order.get_muzzleflashes_items+order.get_shockwaves_items+order.get_particles_items+order.get_environmentvfx_items+order.get_debrisandcracksvfx_items+order.get_lightiningsfx_items+order.get_energysfx_items+order.get_environmentalsfx_items+order.get_firesfx_items+order.get_machinerysfx_items+order.get_weaponsfx_items+order.get_fightingsfx_items+order.get_landscapes_items+order.get_characters_items+order.get_opticallens_items+order.get_audiopack_items+order.get_vfxpack_items+order.get_flimtransitionpack_items+order.get_motiongraphicspack_items+order.get_audiospectrum_items+order.get_lyricstemplate_items
       
    else:
        TotalCartItems=0
        getpaiddebrisandcrackvfx=DebrisandCracksVfx.objects.filter(type="PAID")  
        getfreedebrisandcrackvfx=DebrisandCracksVfx.objects.filter(type="FREE")       

    context={ 
             'TotalCartItems':TotalCartItems,
             'getpaiddebrisandcrackvfx':getpaiddebrisandcrackvfx,
             'getfreedebrisandcrackvfx':getfreedebrisandcrackvfx,   
             }
    return render(request,'VFX/DebrisAndCracks.html',context) 
   
def updatedebrisandcrackvfx(request):
    print('DebrisandCrackVfx(s) loaded to the API..')
    data = json.loads(request.body) 
    productName = data['productName'] 
    publisherId=data['publisherId']
    action = data['action']
    print('action:', action) 
    print('productName:', productName)  
    customer = request.user.customer #locking customer
    product=DebrisandCracksVfx.objects.get(name=productName)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    purchase, created = PurchasedProducts.objects.get_or_create(customer=customer, complete=False)    
    orderdebrisandcrackvfx, created = OrderDebrisAndCracksVfx.objects.get_or_create(customer=customer, order=order, addtoDpage=purchase,published_by=publisherId, product=product,complete=False)
   

    if action == 'add':
        if orderdebrisandcrackvfx.quantity==0:
           orderdebrisandcrackvfx.quantity = (orderdebrisandcrackvfx.quantity + 1)
        elif orderdebrisandcrackvfx.quantity==1:
           orderdebrisandcrackvfx.quantity =orderdebrisandcrackvfx.quantity 
    
    if action == 'remove':
        orderdebrisandcrackvfx.quantity = (orderdebrisandcrackvfx.quantity - 1)

    orderdebrisandcrackvfx.save()

    if orderdebrisandcrackvfx.quantity <=0: #if the orderitem is 0 delete it
        orderdebrisandcrackvfx.delete()

    return JsonResponse('Item was added', safe=False)

