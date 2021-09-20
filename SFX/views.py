from django.shortcuts import render
from EHub.models import *
from SFX.models import *

from django.http import JsonResponse, response
import json        #data = json.loads(request.body) 
import datetime

from django.contrib.auth.decorators import login_required  #Restriciton ofp Pages (For not to display pages for anonymous user(but only logged in users))
from EHub.decorators import unauthenticated_user, allowed_users, admin_only 

#SFX SECTION
def electricitysfx(request):
    if request.user.is_authenticated:
        getpaidlightiningsfx=LightiningSfx.objects.filter(type="PAID")  
        getfreelightiningsfx=LightiningSfx.objects.filter(type="FREE")     
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        TotalCartItems=order.get_lightiningvfx_items+order.get_energyvfx_items+order.get_muzzleflashes_items+order.get_shockwaves_items+order.get_particles_items+order.get_environmentvfx_items+order.get_debrisandcracksvfx_items+order.get_lightiningsfx_items+order.get_energysfx_items+order.get_environmentalsfx_items+order.get_firesfx_items+order.get_machinerysfx_items+order.get_weaponsfx_items+order.get_fightingsfx_items+order.get_landscapes_items+order.get_characters_items+order.get_opticallens_items+order.get_audiopack_items+order.get_vfxpack_items+order.get_flimtransitionpack_items+order.get_motiongraphicspack_items+order.get_audiospectrum_items+order.get_lyricstemplate_items
    else:
        getpaidlightiningsfx=LightiningSfx.objects.filter(type="PAID")  
        getfreelightiningsfx=LightiningSfx.objects.filter(type="FREE")      
        TotalCartItems=0
    context={ 
             'TotalCartItems':TotalCartItems,
             'getpaidlightiningsfx':getpaidlightiningsfx,
             'getfreelightiningsfx':getfreelightiningsfx,   
             }
    return render(request, 'SFX/Electricity.html',context)

def updatelightiningsfx(request):
    print('LightiningSfx(s) loaded to the API..')
    data = json.loads(request.body) # We are recieving  data(item was added) importing from json as a string and we need to parse it so for that we need .loads an we r sending back using request.body
    productName = data['productName'] 
    publisherId=data['publisherId']
    action = data['action']
     #now we wanna print this out after parsing making them available in dictionary
    print('action:', action) 
    
    print('productName:', productName)  

    customer = request.user.customer #locking customer
    getlightiningsfx=LightiningSfx.objects.get(name=productName)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    purchase, created = PurchasedProducts.objects.get_or_create(customer=customer, complete=False)    
    orderlightiningsfx, created = OrderLightiningSfx.objects.get_or_create(customer=customer, published_by=publisherId,order=order, addtoDpage=purchase, product=getlightiningsfx,complete=False)
   
    if action == 'add':
        if orderlightiningsfx.quantity==0:
           orderlightiningsfx.quantity = (orderlightiningsfx.quantity + 1)
        elif orderlightiningsfx.quantity==1:
           orderlightiningsfx.quantity =orderlightiningsfx.quantity 
    
    if action == 'remove':
        orderlightiningsfx.quantity = (orderlightiningsfx.quantity - 1)

    orderlightiningsfx.save()

    if orderlightiningsfx.quantity <=0: #if the orderitem is 0 delete it
        orderlightiningsfx.delete()

    return JsonResponse('Item was added', safe=False)

def firesfx(request):
    if request.user.is_authenticated:
        getpaidfiresfx=FireSfx.objects.filter(type="PAID")  
        getfreefiresfx=FireSfx.objects.filter(type="FREE")     
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        TotalCartItems=order.get_lightiningvfx_items+order.get_energyvfx_items+order.get_muzzleflashes_items+order.get_shockwaves_items+order.get_particles_items+order.get_environmentvfx_items+order.get_debrisandcracksvfx_items+order.get_lightiningsfx_items+order.get_energysfx_items+order.get_environmentalsfx_items+order.get_firesfx_items+order.get_machinerysfx_items+order.get_weaponsfx_items+order.get_fightingsfx_items+order.get_landscapes_items+order.get_characters_items+order.get_opticallens_items+order.get_audiopack_items+order.get_vfxpack_items+order.get_flimtransitionpack_items+order.get_motiongraphicspack_items+order.get_audiospectrum_items+order.get_lyricstemplate_items
       
    else:
        getpaidfiresfx=FireSfx.objects.filter(type="PAID")  
        getfreefiresfx=FireSfx.objects.filter(type="FREE")      
        TotalCartItems=0
    context={ 
             'TotalCartItems':TotalCartItems,
             'getpaidfiresfx':getpaidfiresfx,
             'getfreefiresfx':getfreefiresfx,   
             }
    return render(request,'SFX/Fire.html',context)

def updatefiresfx(request):
    print('FireSfx(s) loaded to the API..')
    data = json.loads(request.body) # We are recieving  data(item was added) importing from json as a string and we need to parse it so for that we need .loads an we r sending back using request.body
    productName = data['productName'] 
    publisherId=data['publisherId']
    action = data['action']
    print('action:', action) 
    print('productName:', productName)  

    customer = request.user.customer #locking customer
    getfiresfx=FireSfx.objects.get(name=productName)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    purchase, created = PurchasedProducts.objects.get_or_create(customer=customer, complete=False)      
    orderfiresfx, created = OrderFireSfx.objects.get_or_create(customer=customer, published_by=publisherId,order=order, addtoDpage=purchase, product=getfiresfx,complete=False)
  
    #INCREASING OR DECREASING QUANTITY OF ORDER ITEM
    if action == 'add':
        if orderfiresfx.quantity==0:
           orderfiresfx.quantity = (orderfiresfx.quantity + 1)
        elif orderfiresfx.quantity==1:
           orderfiresfx.quantity =orderfiresfx.quantity 
    
    if action == 'remove':
        orderfiresfx.quantity = (orderfiresfx.quantity - 1)

    orderfiresfx.save()

    if orderfiresfx.quantity <=0: 
        orderfiresfx.delete()

    return JsonResponse('Item was added', safe=False)

def energysfx(request):
    if request.user.is_authenticated:
        getpaidEnergysfx=EnergySfx.objects.filter(type="PAID")  
        getfreeEnergysfx=EnergySfx.objects.filter(type="FREE")     
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        TotalCartItems=order.get_lightiningvfx_items+order.get_energyvfx_items+order.get_muzzleflashes_items+order.get_shockwaves_items+order.get_particles_items+order.get_environmentvfx_items+order.get_debrisandcracksvfx_items+order.get_lightiningsfx_items+order.get_energysfx_items+order.get_environmentalsfx_items+order.get_firesfx_items+order.get_machinerysfx_items+order.get_weaponsfx_items+order.get_fightingsfx_items+order.get_landscapes_items+order.get_characters_items+order.get_opticallens_items+order.get_audiopack_items+order.get_vfxpack_items+order.get_flimtransitionpack_items+order.get_motiongraphicspack_items+order.get_audiospectrum_items+order.get_lyricstemplate_items
       
    else:
        getpaidEnergysfx=EnergySfx.objects.filter(type="PAID")  
        getfreeEnergysfx=EnergySfx.objects.filter(type="FREE")       
        TotalCartItems=0
    context={ 
             'TotalCartItems':TotalCartItems,
             'getpaidEnergysfx':getpaidEnergysfx,
             'getfreeEnergysfx':getfreeEnergysfx,   
             }
    return render(request,'SFX/Energy.html',context) 

def updateEnergysfx(request):
    print('EnergySfx(s) loaded to the API..')
    data = json.loads(request.body) # We are recieving  data(item was added) importing from json as a string and we need to parse it so for that we need .loads an we r sending back using request.body
    productName = data['productName']
    publisherId=data['publisherId'] 
    action = data['action']
    print('action:', action) 
    print('productName:', productName)  

    customer = request.user.customer #locking customer
    getEnergysfx=EnergySfx.objects.get(name=productName)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    purchase, created = PurchasedProducts.objects.get_or_create(customer=customer, complete=False)      
    orderEnergySfx, created = OrderEnergySfx.objects.get_or_create(customer=customer, published_by=publisherId ,order=order, addtoDpage=purchase, product=getEnergysfx,complete=False)
  
    #INCREASING OR DECREASING QUANTITY OF ORDER ITEM
    if action == 'add':
        if orderEnergySfx.quantity==0:
           orderEnergySfx.quantity = (orderEnergySfx.quantity + 1)
        elif orderEnergySfx.quantity==1:
           orderEnergySfx.quantity =orderEnergySfx.quantity 
    
    if action == 'remove':
        orderEnergySfx.quantity = (orderEnergySfx.quantity - 1)

    orderEnergySfx.save()

    if orderEnergySfx.quantity <=0: 
        orderEnergySfx.delete()

    return JsonResponse('Item was added', safe=False)

def environmentalsfx(request): 
    if request.user.is_authenticated:
        getpaidWhoosesSfx=EnvironmentalSfx.objects.filter(type="PAID")  
        getfreeWhoosesSfx=EnvironmentalSfx.objects.filter(type="FREE")     
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        TotalCartItems=order.get_lightiningvfx_items+order.get_energyvfx_items+order.get_muzzleflashes_items+order.get_shockwaves_items+order.get_particles_items+order.get_environmentvfx_items+order.get_debrisandcracksvfx_items+order.get_lightiningsfx_items+order.get_energysfx_items+order.get_environmentalsfx_items+order.get_firesfx_items+order.get_machinerysfx_items+order.get_weaponsfx_items+order.get_fightingsfx_items+order.get_landscapes_items+order.get_characters_items+order.get_opticallens_items+order.get_audiopack_items+order.get_vfxpack_items+order.get_flimtransitionpack_items+order.get_motiongraphicspack_items+order.get_audiospectrum_items+order.get_lyricstemplate_items
       
    else:
        getpaidWhoosesSfx=EnvironmentalSfx.objects.filter(type="PAID")  
        getfreeWhoosesSfx=EnvironmentalSfx.objects.filter(type="FREE")  
        TotalCartItems=0
    context={ 
             'TotalCartItems':TotalCartItems,
             'getpaidWhoosesSfx':getpaidWhoosesSfx,
             'getfreeWhoosesSfx':getfreeWhoosesSfx,   
             }
    return render(request,'SFX/Environmentalsfx.html',context)

def updateenvironmentalsfx(request):
    print('EnvironmentalSfx(s) loaded to the API..')
    data = json.loads(request.body) # We are recieving  data(item was added) importing from json as a string and we need to parse it so for that we need .loads an we r sending back using request.body
    productName = data['productName'] 
    publisherId=data['publisherId']
    action = data['action']
    print('action:', action) 
    print('productName:', productName)  

    customer = request.user.customer #locking customer
    getEnvironmentalsfx=EnvironmentalSfx.objects.get(name=productName)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    purchase, created = PurchasedProducts.objects.get_or_create(customer=customer, complete=False)      
    orderEnvironmentalSfx, created = OrderEnvironmentalSfx.objects.get_or_create(customer=customer, published_by=publisherId ,order=order, addtoDpage=purchase, product=getEnvironmentalsfx,complete=False)
  
    #INCREASING OR DECREASING QUANTITY OF ORDER ITEM
    if action == 'add':
        if orderEnvironmentalSfx.quantity==0:
           orderEnvironmentalSfx.quantity = (orderEnvironmentalSfx.quantity + 1)
        elif orderEnvironmentalSfx.quantity==1:
           orderEnvironmentalSfx.quantity =orderEnvironmentalSfx.quantity 
    
    if action == 'remove':
        orderEnvironmentalSfx.quantity = (orderEnvironmentalSfx.quantity - 1)

    orderEnvironmentalSfx.save()

    if orderEnvironmentalSfx.quantity <=0: 
        orderEnvironmentalSfx.delete()

    return JsonResponse('Item was added', safe=False)

def machinerysfx(request):
    if request.user.is_authenticated:
        getpaidMachinerySfx=MachinerySfx.objects.filter(type="PAID")  
        getfreeMachinerySfx=MachinerySfx.objects.filter(type="FREE")     
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        TotalCartItems=order.get_lightiningvfx_items+order.get_energyvfx_items+order.get_muzzleflashes_items+order.get_shockwaves_items+order.get_particles_items+order.get_environmentvfx_items+order.get_debrisandcracksvfx_items+order.get_lightiningsfx_items+order.get_energysfx_items+order.get_environmentalsfx_items+order.get_firesfx_items+order.get_machinerysfx_items+order.get_weaponsfx_items+order.get_fightingsfx_items+order.get_landscapes_items+order.get_characters_items+order.get_opticallens_items+order.get_audiopack_items+order.get_vfxpack_items+order.get_flimtransitionpack_items+order.get_motiongraphicspack_items+order.get_audiospectrum_items+order.get_lyricstemplate_items
       
    else:
        getpaidMachinerySfx=MachinerySfx.objects.filter(type="PAID")  
        getfreeMachinerySfx=MachinerySfx.objects.filter(type="FREE")   
        TotalCartItems=0
    context={ 
             'TotalCartItems':TotalCartItems,
             'getpaidMachinerySfx':getpaidMachinerySfx,
             'getfreeMachinerySfx':getfreeMachinerySfx,   
             }
    return render(request,'SFX/Machinery.html',context)

def updatemachinerysfx(request):
    print('MachinerySfx(s) loaded to the API..')
    data = json.loads(request.body) # We are recieving  data(item was added) importing from json as a string and we need to parse it so for that we need .loads an we r sending back using request.body
    productName = data['productName'] 
    publisherId=data['publisherId']
    action = data['action']
    print('action:', action) 
    print('productName:', productName)  

    customer = request.user.customer #locking customer
    getMachinerysfx=MachinerySfx.objects.get(name=productName)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    purchase, created = PurchasedProducts.objects.get_or_create(customer=customer, complete=False)    
    orderMachinerySfx, created = OrderMachinerySfx.objects.get_or_create(customer=customer, order=order, addtoDpage=purchase,published_by=publisherId, product=getMachinerysfx,complete=False)
  
    #INCREASING OR DECREASING QUANTITY OF ORDER ITEM
    if action == 'add':
        if orderMachinerySfx.quantity==0:
           orderMachinerySfx.quantity = (orderMachinerySfx.quantity + 1)
        elif orderMachinerySfx.quantity==1:
           orderMachinerySfx.quantity =orderMachinerySfx.quantity 
    
    if action == 'remove':
        orderMachinerySfx.quantity = (orderMachinerySfx.quantity - 1)

    orderMachinerySfx.save()

    if orderMachinerySfx.quantity <=0: 
        orderMachinerySfx.delete()

    return JsonResponse('Item was added', safe=False)

def weaponsfx(request): 
    if request.user.is_authenticated:
        getpaidWeaponSfx=WeaponsSfx.objects.filter(type="PAID")  
        getfreeWeaponSfx=WeaponsSfx.objects.filter(type="FREE")     
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        TotalCartItems=order.get_lightiningvfx_items+order.get_energyvfx_items+order.get_muzzleflashes_items+order.get_shockwaves_items+order.get_particles_items+order.get_environmentvfx_items+order.get_debrisandcracksvfx_items+order.get_lightiningsfx_items+order.get_energysfx_items+order.get_environmentalsfx_items+order.get_firesfx_items+order.get_machinerysfx_items+order.get_weaponsfx_items+order.get_fightingsfx_items+order.get_landscapes_items+order.get_characters_items+order.get_opticallens_items+order.get_audiopack_items+order.get_vfxpack_items+order.get_flimtransitionpack_items+order.get_motiongraphicspack_items+order.get_audiospectrum_items+order.get_lyricstemplate_items
       
    else:
        getpaidWeaponSfx=WeaponsSfx.objects.filter(type="PAID")  
        getfreeWeaponSfx=WeaponsSfx.objects.filter(type="FREE")  
        TotalCartItems=0
    context={ 
             'TotalCartItems':TotalCartItems,
             'getpaidWeaponSfx':getpaidWeaponSfx,
             'getfreeWeaponSfx':getfreeWeaponSfx,   
             }
    return render(request,'SFX/WeaponSfx.html',context)

def updateweaponsfx(request):
    print('WeaponSfx(s) loaded to the API..')
    data = json.loads(request.body) # We are recieving  data(item was added) importing from json as a string and we need to parse it so for that we need .loads an we r sending back using request.body
    productName = data['productName'] 
    publisherId=data['publisherId']
    action = data['action']
    print('action:', action) 
    print('productName:', productName)  

    customer = request.user.customer #locking customer
    getWeaponsfx=WeaponsSfx.objects.get(name=productName)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    purchase, created = PurchasedProducts.objects.get_or_create(customer=customer, complete=False)      
    orderweaponsfx, created = OrderWeaponsSfx.objects.get_or_create(customer=customer, published_by=publisherId,order=order, addtoDpage=purchase, product=getWeaponsfx,complete=False)
  
    #INCREASING OR DECREASING QUANTITY OF ORDER ITEM
    if action == 'add':
        if orderweaponsfx.quantity==0:
           orderweaponsfx.quantity = (orderweaponsfx.quantity + 1)
        elif orderweaponsfx.quantity==1:
           orderweaponsfx.quantity =orderweaponsfx.quantity 
    
    if action == 'remove':
        orderweaponsfx.quantity = (orderweaponsfx.quantity - 1)

    orderweaponsfx.save()

    if orderweaponsfx.quantity <=0: 
        orderweaponsfx.delete()

    return JsonResponse('Item was added', safe=False)

def fightingsfx(request):
    if request.user.is_authenticated:
        getpaidFightingSfx=FightingSfx.objects.filter(type="PAID")  
        getfreeFightingSfx=FightingSfx.objects.filter(type="FREE")     
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        TotalCartItems=order.get_lightiningvfx_items+order.get_energyvfx_items+order.get_muzzleflashes_items+order.get_shockwaves_items+order.get_particles_items+order.get_environmentvfx_items+order.get_debrisandcracksvfx_items+order.get_lightiningsfx_items+order.get_energysfx_items+order.get_environmentalsfx_items+order.get_firesfx_items+order.get_machinerysfx_items+order.get_weaponsfx_items+order.get_fightingsfx_items+order.get_landscapes_items+order.get_characters_items+order.get_opticallens_items+order.get_audiopack_items+order.get_vfxpack_items+order.get_flimtransitionpack_items+order.get_motiongraphicspack_items+order.get_audiospectrum_items+order.get_lyricstemplate_items
       
    else:
        getpaidFightingSfx=FightingSfx.objects.filter(type="PAID")  
        getfreeFightingSfx=FightingSfx.objects.filter(type="FREE")   
        TotalCartItems=0
    context={ 
             'TotalCartItems':TotalCartItems,
             'getpaidFightingSfx':getpaidFightingSfx,
             'getfreeFightingSfx':getfreeFightingSfx,   
             }
    return render(request,'SFX/FightingSfx.html',context)

def updatefightingsfx(request):
    print('FightingSfx(s) loaded to the API..')
    data = json.loads(request.body) # We are recieving  data(item was added) importing from json as a string and we need to parse it so for that we need .loads an we r sending back using request.body
    productName = data['productName'] 
    publisherId=data['publisherId']
    action = data['action']
    print('action:', action) 
    print('productName:', productName)  

    customer = request.user.customer #locking customer
    getFightingsfx=FightingSfx.objects.get(name=productName)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    purchase, created = PurchasedProducts.objects.get_or_create(customer=customer, complete=False)      
    orderfightingsfx, created = OrderFightingSfx.objects.get_or_create(customer=customer, published_by=publisherId,order=order, addtoDpage=purchase, product=getFightingsfx,complete=False)
  
    #INCREASING OR DECREASING QUANTITY OF ORDER ITEM
    if action == 'add':
        if orderfightingsfx.quantity==0:
           orderfightingsfx.quantity = (orderfightingsfx.quantity + 1)
        elif orderfightingsfx.quantity==1:
           orderfightingsfx.quantity =orderfightingsfx.quantity 
    
    if action == 'remove':
        orderfightingsfx.quantity = (orderfightingsfx.quantity - 1)

    orderfightingsfx.save()

    if orderfightingsfx.quantity <=0: 
        orderfightingsfx.delete()

    return JsonResponse('Item was added', safe=False)