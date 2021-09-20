from VFX.models import *
from SFX.models import *
from OTHERS.models import *
from GraphicsElements.models import *
from SpecialPacks.models import *
from .models import *
from django.shortcuts import render,redirect,HttpResponse
import requests
from django.views.generic import View
from requests.models import requote_uri

from django.http import JsonResponse, response
import json              # data = json.loads(request.body) 
import datetime

from django.contrib.auth.decorators import login_required  #Restriciton ofp Pages (For not to display pages for anonymous user(but only logged in users))
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .decorators import unauthenticated_user, allowed_users, admin_only  #Maintaining privacy(pages that are restricted and allowed to common users )

from django.contrib.auth.admin import Group

import uuid
#for sending email
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail

from .forms import *

# Create your views here.
#@login_required(login_url='login')  
def Home(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		#Imp note:-when payment is done of order a new order is created but no get from database
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		purchase, created = PurchasedProducts.objects.get_or_create(customer=customer, complete=False)
	  
		TotalCartItems=order.get_lightiningvfx_items+order.get_energyvfx_items+order.get_muzzleflashes_items+order.get_shockwaves_items+order.get_particles_items+order.get_environmentvfx_items+order.get_debrisandcracksvfx_items+order.get_lightiningsfx_items+order.get_energysfx_items+order.get_environmentalsfx_items+order.get_firesfx_items+order.get_machinerysfx_items+order.get_weaponsfx_items+order.get_fightingsfx_items+order.get_landscapes_items+order.get_characters_items+order.get_opticallens_items+order.get_audiopack_items+order.get_vfxpack_items+order.get_flimtransitionpack_items+order.get_motiongraphicspack_items+order.get_audiospectrum_items+order.get_lyricstemplate_items
	  
		getpaidlightiningsfx=LightiningSfx.objects.filter(type="PAID")  
		getfreelightiningsfx=LightiningSfx.objects.filter(type="FREE") 
		getpaidEnergysfx=EnergySfx.objects.filter(type="PAID")  
		getfreeEnergysfx=EnergySfx.objects.filter(type="FREE")  
		getpaidMachinerySfx=MachinerySfx.objects.filter(type="PAID")  
		getfreeMachinerySfx=MachinerySfx.objects.filter(type="FREE")    
			
		getpaidlightiningvfx=LightiningVfx.objects.filter(type="PAID")  
		getfreelightiningvfx=LightiningVfx.objects.filter(type="FREE")      
							
		getpaidEnergyvfx=EnergyVfx.objects.filter(type="PAID")  
		getfreeEnergyvfx=EnergyVfx.objects.filter(type="FREE")      
	else:
		order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping':False } 
		getpaidlightiningsfx=LightiningSfx.objects.filter(type="PAID")  
		getfreelightiningsfx=LightiningSfx.objects.filter(type="FREE")
		getpaidEnergysfx=EnergySfx.objects.filter(type="PAID")  
		getfreeEnergysfx=EnergySfx.objects.filter(type="FREE") 
		getpaidMachinerySfx=MachinerySfx.objects.filter(type="PAID")  
		getfreeMachinerySfx=MachinerySfx.objects.filter(type="FREE") 
					 
		getpaidlightiningvfx=LightiningVfx.objects.filter(type="PAID")  
		getfreelightiningvfx=LightiningVfx.objects.filter(type="FREE")     
		getpaidEnergyvfx=EnergyVfx.objects.filter(type="PAID")  
		getfreeEnergyvfx=EnergyVfx.objects.filter(type="FREE")            
	  
		TotalCartItems = 0 

	context={
			 'TotalCartItems':TotalCartItems,
			 
			 'getpaidEnergyvfx':getpaidEnergyvfx,
			 'getfreeEnergyvfx':getfreeEnergyvfx,   
			 
			 'getpaidlightiningvfx':getpaidlightiningvfx,
			 'getfreelightiningvfx':getfreelightiningvfx,   
			 
			  'getpaidlightiningsfx':getpaidlightiningsfx,
			  'getfreelightiningsfx':getfreelightiningsfx,   
			  'getpaidEnergysfx':getpaidEnergysfx,
			  'getfreeEnergysfx':getfreeEnergysfx,   
			  'getpaidMachinerySfx':getpaidMachinerySfx,
			  'getfreeMachinerySfx':getfreeMachinerySfx,   
			 }
	return render(request,'frontend_base.html',context)

def ContactApi(request):
	if request.method=="POST":
		name=request.POST['name']
		email=request.POST['email']
		title=request.POST['title']
		content =request.POST['content']
		if len(name)<=2 and len(title)<=4 and len(content)<=9:
			messages.error(request, "Please fill the form correctly")
		else:
			contact=Contact(name=name, email=email, title=title, content=content)
			contact.save()
			messages.success(request, "Your message has been successfully sent")  
			
	return render(request, "E-HUB/contact.html")

def SearchEngine(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		TotalCartAmount=order.get_lightiningvfx_total+order.get_energyvfx_total+order.get_muzzleflashes_total+order.get_shockwaves_total+order.get_particles_total+order.get_environmentvfx_total+order.get_debrisandcracksvfx_total+order.get_lightiningsfx_total+order.get_energysfx_total+order.get_environmentalsfx_total+order.get_firesfx_total+order.get_machinerysfx_total+order.get_weaponsfx_total+order.get_fightingsfx_total+order.get_landscapes_total+order.get_characters_total+order.get_opticallens_total+order.get_audiopack_total+order.get_vfxpack_total+order.get_flimtransitionpack_total+order.get_motiongraphicspack_total+order.get_audiospectrum_total+order.get_lyricstemplate_total
	  
	else:
		TotalCartAmount=0
		order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping':False }    
		
	query=request.GET['query']
	if len(query)>78 or  len(query)<3 or len(query)==0 : 
	  #SPECIAL PACKS
		getfreesoundpacks=SoundPack.objects.none()
		getpaidsoundpacks=SoundPack.objects.none()
		getfreevfxpacks=VfxPack.objects.none()    
		getpaidvfxpacks=VfxPack.objects.none()    
		getfreeflimtransitionpacks=FlimTransitionPack.objects.none()    
		getpaidflimtransitionpacks=FlimTransitionPack.objects.none()
		getfreemotiongraphicspacks=MotionGraphicsPack.objects.none()    
		getpaidmotiongraphicspacks=MotionGraphicsPack.objects.none()             
		  
	   #OTHERS
		getfreeaudiospectrums=AudioSpectrum.objects.none()        
		getpaidaudiospectrums=AudioSpectrum.objects.none()      
		getfreelyricstemplate=LyricsTemplate.objects.none()        
		getpaidlyricstemplate=LyricsTemplate.objects.none()     
				
		#SFX
		getfreelightiningsfx=LightiningSfx.objects.none()       
		getpaidlightiningsfx=LightiningSfx.objects.none() 
		  
		getfreeEnergysfx=EnergySfx.objects.none()              
		getpaidEnergysfx=EnergySfx.objects.none()    
		
		getfreeEnvironmentalsfx=EnvironmentalSfx.objects.none()     
		getpaidEnvironmentalsfx=EnvironmentalSfx.objects.none()     
	   
		getfreeFiresfx=FireSfx.objects.none()     
		getpaidFiresfx=FireSfx.objects.none()  
		
		getfreeWeaponsfx=WeaponsSfx.objects.none()     
		getpaidWeaponsfx=WeaponsSfx.objects.none()       
		
		getfreeFightiningsfx=FightingSfx.objects.none()     
		getpaidFightiningsfx=FightingSfx.objects.none()  
		
		getfreeMachinerysfx=MachinerySfx.objects.none()     
		getpaidMachinerysfx=MachinerySfx.objects.none()        
								
	   #VFX   
		getfreelightiningvfx=LightiningVfx.objects.none()       
		getpaidlightiningvfx=LightiningVfx.objects.none()      
		
		getfreeEnergyvfx=EnergyVfx.objects.none()              
		getpaidEnergyvfx=EnergyVfx.objects.none()    
 
		getfreeMuzzleFlashes=MuzzleFlahses.objects.none()     
		getpaidMuzzleFlashes=MuzzleFlahses.objects.none()  
		
		getfreeShockwavesVfx=ShockwavesVfx.objects.none()     
		getpaidShockwavesVfx=ShockwavesVfx.objects.none()       
		
		getfreeParticleVfx=ParticlesVfx.objects.none()     
		getpaidParticleVfx=ParticlesVfx.objects.none()  
		
		getfreeEnvironmentalVfx=EnvironmentalVfx.objects.none()     
		getpaidEnvironmentalVfx=EnvironmentalVfx.objects.none()                   
   
		getfreeDebrisAndCrackVfx=DebrisandCracksVfx.objects.none()     
		getpaidDebrisAndCrackVfx=DebrisandCracksVfx.objects.none()  
			  
		#GRAPHICS ELEMENT        
		getfreelandscapes=Landscapes.objects.none()        
		getpaidlandscapes=Landscapes.objects.none()   
	 
		getfreecharacters=Characters.objects.none()        
		getpaidcharacters=Characters.objects.none()        
	
		getfreeopticallens=Characters.objects.none()        
		getpaidopticallens=Characters.objects.none()       
				 
		countVfxandSfx=getpaidEnergyvfx.union(getfreeEnergyvfx,getpaidlightiningvfx,getfreelightiningvfx,getfreeEnvironmentalVfx,getpaidEnvironmentalVfx,
									getpaidMuzzleFlashes,getfreeMuzzleFlashes,getfreeShockwavesVfx,getpaidShockwavesVfx,getpaidParticleVfx,getfreeParticleVfx,getpaidDebrisAndCrackVfx,getfreeDebrisAndCrackVfx,
									getfreelightiningsfx,getpaidlightiningsfx,getpaidFiresfx,getfreeFiresfx,getfreeEnergysfx,getpaidEnergysfx,getfreeMachinerysfx,getpaidMachinerysfx,getfreeWeaponsfx,getpaidWeaponsfx,getfreeEnvironmentalsfx,getpaidEnvironmentalsfx,getfreeFightiningsfx,getpaidFightiningsfx).count()
		countSpecialPacksAndOthers=getpaidsoundpacks.union(getfreesoundpacks,getfreevfxpacks,getpaidvfxpacks,getfreemotiongraphicspacks,getpaidmotiongraphicspacks,getfreeflimtransitionpacks,getpaidflimtransitionpacks,
														   getfreeaudiospectrums,getpaidaudiospectrums,getfreelyricstemplate,getpaidlyricstemplate).count()
	   
		countGraphicsElements=getpaidlandscapes.union(getfreelandscapes,getfreecharacters,getpaidcharacters,getfreeopticallens,getpaidopticallens).count()
		
		TotalCount=countVfxandSfx+countSpecialPacksAndOthers+countGraphicsElements
	
	else:
		getpaidsoundpacks = SoundPack.objects.filter(name__icontains=query,type="PAID") 
		getfreesoundpacks = SoundPack.objects.filter(name__icontains=query,type="FREE") 
	  
		getfreevfxpacks=VfxPack.objects.filter(name__icontains=query,type="FREE")    
		getpaidvfxpacks=VfxPack.objects.filter(name__icontains=query,type="PAID")    
	  
		getfreeflimtransitionpacks=FlimTransitionPack.objects.filter(name__icontains=query,type="FREE")    
		getpaidflimtransitionpacks=FlimTransitionPack.objects.filter(name__icontains=query,type="PAID")
	  
		getfreemotiongraphicspacks=MotionGraphicsPack.objects.filter(name__icontains=query,type="FREE")    
		getpaidmotiongraphicspacks=MotionGraphicsPack.objects.filter(name__icontains=query,type="PAID")                 

	#GRAPHICS ELEMENT        
		getfreelandscapes=Landscapes.objects.filter(name__icontains=query,type="FREE")        
		getpaidlandscapes=Landscapes.objects.filter(name__icontains=query,type="PAID")   
	 
		getfreecharacters=Characters.objects.filter(name__icontains=query,type="FREE")        
		getpaidcharacters=Characters.objects.filter(name__icontains=query,type="PAID")        
	
		getfreeopticallens=OpticalLens.objects.filter(name__icontains=query,type="FREE")        
		getpaidopticallens=OpticalLens.objects.filter(name__icontains=query,type="PAID")     

 #OTHERS         
		getfreeaudiospectrums=AudioSpectrum.objects.filter(name__icontains=query,type="FREE") 
		getpaidaudiospectrums=AudioSpectrum.objects.filter(name__icontains=query,type="PAID")     
	   
		getfreelyricstemplate=LyricsTemplate.objects.filter(name__icontains=query,type="FREE")        
		getpaidlyricstemplate=LyricsTemplate.objects.filter(name__icontains=query,type="PAID")              
			 
 
 #SFX
		getfreelightiningsfx=LightiningSfx.objects.filter(name__icontains=query,type="FREE")       
		getpaidlightiningsfx=LightiningSfx.objects.filter(name__icontains=query,type="PAID") 
		  
		getfreeEnergysfx=EnergySfx.objects.filter(name__icontains=query,type="FREE")              
		getpaidEnergysfx=EnergySfx.objects.filter(name__icontains=query,type="PAID")    
		
		getfreeEnvironmentalsfx=EnvironmentalSfx.objects.filter(name__icontains=query,type="FREE")     
		getpaidEnvironmentalsfx=EnvironmentalSfx.objects.filter(name__icontains=query,type="PAID")     
	   
		getfreeFiresfx=FireSfx.objects.filter(name__icontains=query,type="FREE")     
		getpaidFiresfx=FireSfx.objects.filter(name__icontains=query,type="PAID")  
		
		getfreeWeaponsfx=WeaponsSfx.objects.filter(name__icontains=query,type="FREE")     
		getpaidWeaponsfx=WeaponsSfx.objects.filter(name__icontains=query,type="PAID")       
		
		getfreeFightiningsfx=FightingSfx.objects.filter(name__icontains=query,type="FREE")     
		getpaidFightiningsfx=FightingSfx.objects.filter(name__icontains=query,type="PAID")  
		
		getfreeMachinerysfx=MachinerySfx.objects.filter(name__icontains=query,type="FREE")     
		getpaidMachinerysfx=MachinerySfx.objects.filter(name__icontains=query,type="PAID") 
									   
 #VFX   
		getfreelightiningvfx=LightiningVfx.objects.filter(name__icontains=query,type="FREE")       
		getpaidlightiningvfx=LightiningVfx.objects.filter(name__icontains=query,type="PAID")      
		
		getfreeEnergyvfx=EnergyVfx.objects.filter(name__icontains=query,type="FREE")              
		getpaidEnergyvfx=EnergyVfx.objects.filter(name__icontains=query,type="PAID")  

		getfreeMuzzleFlashes=MuzzleFlahses.objects.filter(name__icontains=query,type="FREE")     
		getpaidMuzzleFlashes=MuzzleFlahses.objects.filter(name__icontains=query,type="PAID")  
		
		getfreeShockwavesVfx=ShockwavesVfx.objects.filter(name__icontains=query,type="FREE")     
		getpaidShockwavesVfx=ShockwavesVfx.objects.filter(name__icontains=query,type="PAID")       
		
		getfreeParticleVfx=ParticlesVfx.objects.filter(name__icontains=query,type="FREE")     
		getpaidParticleVfx=ParticlesVfx.objects.filter(name__icontains=query,type="PAID")  
		
		getfreeEnvironmentalVfx=EnvironmentalVfx.objects.filter(name__icontains=query,type="FREE")     
		getpaidEnvironmentalVfx=EnvironmentalVfx.objects.filter(name__icontains=query,type="PAID")                   
   
		getfreeDebrisAndCrackVfx=DebrisandCracksVfx.objects.filter(name__icontains=query,type="FREE")     
		getpaidDebrisAndCrackVfx=DebrisandCracksVfx.objects.filter(name__icontains=query,type="PAID")         
				
		countVfxandSfx=getpaidEnergyvfx.union(getfreeEnergyvfx,getpaidlightiningvfx,getfreelightiningvfx,getfreeEnvironmentalVfx,getpaidEnvironmentalVfx,
									getpaidMuzzleFlashes,getfreeMuzzleFlashes,getfreeShockwavesVfx,getpaidShockwavesVfx,getpaidParticleVfx,getfreeParticleVfx,getpaidDebrisAndCrackVfx,getfreeDebrisAndCrackVfx,
									getfreelightiningsfx,getpaidlightiningsfx,getpaidFiresfx,getfreeFiresfx,getfreeEnergysfx,getpaidEnergysfx,getfreeMachinerysfx,getpaidMachinerysfx,getfreeWeaponsfx,getpaidWeaponsfx,getfreeEnvironmentalsfx,getpaidEnvironmentalsfx,getfreeFightiningsfx,getpaidFightiningsfx).count()
		countSpecialPacksAndOthers=getpaidsoundpacks.union(getfreesoundpacks,getfreevfxpacks,getpaidvfxpacks,getfreemotiongraphicspacks,getpaidmotiongraphicspacks,getfreeflimtransitionpacks,getpaidflimtransitionpacks,
														   getfreeaudiospectrums,getpaidaudiospectrums,getfreelyricstemplate,getpaidlyricstemplate).count()
		countGraphicsElements=getpaidlandscapes.union(getfreelandscapes,getfreecharacters,getpaidcharacters,getfreeopticallens,getpaidopticallens).count()
		
		TotalCount=countVfxandSfx+countSpecialPacksAndOthers+countGraphicsElements
	print(TotalCount)
	print(countVfxandSfx)
	print(countSpecialPacksAndOthers)
	params={
		   'countVfxandSfx':countVfxandSfx,
		   'countSpecialPacksAndOthers':countSpecialPacksAndOthers,
		   'TotalCount':TotalCount,
 #OTHERS           
		   'getpaidaudiospectrums':getpaidaudiospectrums,
		   'getfreeaudiospectrums':getfreeaudiospectrums,   
		   
		   'getfreelyricstemplate':getfreelyricstemplate,
		   'getpaidlyricstemplate':getpaidlyricstemplate,
		   
 #GRAPHICS ELEMETNS           
			'getpaidlandscapes':getpaidlandscapes,
			'getfreelandscapes':getfreelandscapes,   
		   
		   'getfreecharacters':getfreecharacters,
		   'getpaidcharacters':getpaidcharacters,       
		   
			'getfreeopticallens':getfreeopticallens,
		   'getpaidopticallens':getpaidopticallens,           
					  
 #SPECIAL PACKS           
		   'getfreesoundpacks':getfreesoundpacks,
		   'getpaidsoundpacks':getpaidsoundpacks,
		   
		   'getfreevfxpacks':getfreevfxpacks,
		   'getpaidvfxpacks': getpaidvfxpacks,
		   
		   'getfreeflimtransitionpacks':getfreeflimtransitionpacks,
		   'getpaidflimtransitionpacks':getpaidflimtransitionpacks,
		   
		   'getfreemotiongraphicspacks':getfreemotiongraphicspacks,
		   'getpaidmotiongraphicspacks':getpaidmotiongraphicspacks,
 #SFX
		   ' getfreelightiningsfx': getfreelightiningsfx,
		   'getpaidlightiningsfx':getpaidlightiningsfx,
		   
		   'getfreeEnergysfx':getfreeEnergysfx,
		   ' getpaidEnergysfx': getpaidEnergysfx,
		   
		   'getfreeFiresfx': getfreeFiresfx,
		   'getpaidFiresfx':getpaidFiresfx,
		   
		   'getfreeMachinerysfx': getfreeMachinerysfx,
		   'getpaidMachinerysfx':getpaidMachinerysfx,
		   
		   ' getfreeWeaponsfx': getfreeWeaponsfx,
		   'getpaidWeaponsfx':getpaidWeaponsfx,
		   
		   'getfreeFightiningsfx':getfreeFightiningsfx,
		   'getpaidFightiningsfx':getpaidFightiningsfx,
		   
		   'getfreeEnvironmentalsfx':getfreeEnvironmentalsfx,
		   'getpaidEnvironmentalsfx':getpaidEnvironmentalsfx,
 #VFX           
		   'getfreelightiningvfx': getfreelightiningvfx,
		   'getpaidlightiningvfx':getpaidlightiningvfx,
		   
		   'getfreeEnergyvfx':getfreeEnergyvfx,
		   'getpaidEnergyvfx': getpaidEnergyvfx,
		   
		   'getfreeMuzzleFlashes':getfreeMuzzleFlashes,
		   'getpaidMuzzleFlashes':getpaidMuzzleFlashes,
		   
		   'getfreeShockwavesVfx':getfreeShockwavesVfx,
		   'getpaidShockwavesVfx':getpaidShockwavesVfx,
		   
		   'getfreeParticleVfx':getfreeParticleVfx,
		   'getpaidParticleVfx':getpaidParticleVfx,
		   
		   'getfreeEnvironmentalVfx':getfreeEnvironmentalVfx,
		   'getpaidEnvironmentalVfx':getpaidEnvironmentalVfx,
		   
		   'getfreeDebrisAndCrackVfx':getfreeDebrisAndCrackVfx,
		   'getpaidDebrisAndCrackVfx':getpaidDebrisAndCrackVfx,
		   
		   'query': query, 
		   'TotalCartAmount': TotalCartAmount,            

		   }
	return render(request, 'search.html', params)

@login_required(login_url='login')
def YourCart(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		
		#this  is how we display cart items of particular user
		#OTHERS
		renderaudiospectrums = order.orderaudiospectrum_set.all()
		renderlyricstemplates = order.orderlyricstemplates_set.all()
		
		#SPECIALPACKS
		renderaudiopack=order.ordersoundpack_set.all()
		rendervfxpack=order.ordervfxpack_set.all()
		renderflimtransitionpack=order.orderflimtransition_set.all()        
		rendermotiongraphicspack=order.ordermotiongraphicspack_set.all()
				
		#GRAPHICS ELEMENTS
		renderlandscapes = order.orderlandscape_set.all()
		rendercharacters = order.ordercharacter_set.all()
		renderopticallens = order.orderopticallense_set.all()  
		
		#SFX
		renderlightiningsfx=order.orderlightiningsfx_set.all()
		renderenvironmentalsfx=order.orderenvironmentalsfx_set.all()        
		renderfiresfx=order.orderfiresfx_set.all()
		renderenergysfx=order.orderenergysfx_set.all()    
		renderfightiningsfx=order.orderfightingsfx_set.all()        
		renderweaponsfx=order.orderweaponssfx_set.all()
		rendermachinerysfx=order.ordermachinerysfx_set.all()              
			 
		#VFX
		renderenergyvfx=order.orderenergyvfx_set.all()
		renderlightiningvfx=order.orderlightiningvfx_set.all()    
		rendermuzzleflashesvfx=order.ordermuzzleflashesvfx_set.all()
		rendershockwavesvfx=order.ordershockwavesvfx_set.all()   
		renderparticlevfx=order.orderparticlevfx_set.all()
		renderenvironmentalvfx=order.orderenvironmentalvfx_set.all() 
		renderdebrisandcrackvfx=order.orderdebrisandcracksvfx_set.all()
		  
			 
		TotalCartAmount=order.get_lightiningvfx_total+order.get_energyvfx_total+order.get_muzzleflashes_total+order.get_shockwaves_total+order.get_particles_total+order.get_environmentvfx_total+order.get_debrisandcracksvfx_total+order.get_lightiningsfx_total+order.get_energysfx_total+order.get_environmentalsfx_total+order.get_firesfx_total+order.get_machinerysfx_total+order.get_weaponsfx_total+order.get_fightingsfx_total+order.get_landscapes_total+order.get_characters_total+order.get_opticallens_total+order.get_audiopack_total+order.get_vfxpack_total+order.get_flimtransitionpack_total+order.get_motiongraphicspack_total+order.get_audiospectrum_total+order.get_lyricstemplate_total
		TotalCartItems=order.get_lightiningvfx_items+order.get_energyvfx_items+order.get_muzzleflashes_items+order.get_shockwaves_items+order.get_particles_items+order.get_environmentvfx_items+order.get_debrisandcracksvfx_items+order.get_lightiningsfx_items+order.get_energysfx_items+order.get_environmentalsfx_items+order.get_firesfx_items+order.get_machinerysfx_items+order.get_weaponsfx_items+order.get_fightingsfx_items+order.get_landscapes_items+order.get_characters_items+order.get_opticallens_items+order.get_audiopack_items+order.get_vfxpack_items+order.get_flimtransitionpack_items+order.get_motiongraphicspack_items+order.get_audiospectrum_items+order.get_lyricstemplate_items
	   
		print(TotalCartAmount)
		print(TotalCartItems)
		
	else:
		items = []
		order = {'get_cart_total': 0,'TotalCartAmount':0,'TotalCartItems':0, 'get_cart_items': 0, 'shipping':False }  #if you logout from database and reload the server page it's gonna show errror so to solve this..
	
	context = {
			  #Others
			  'renderaudiospectrums':renderaudiospectrums,
			  'renderlyricstemplates':renderlyricstemplates,
			  
			  #SpecialPacks
			  'renderaudiopack': renderaudiopack,
			  'rendervfxpack':rendervfxpack,
			  'renderflimtransitionpack':renderflimtransitionpack,
			  'rendermotiongraphicspack':rendermotiongraphicspack,
			  
			  #GRAPHICS ELEMENTS
			  'renderlandscapes':renderlandscapes,
			  'rendercharacters':rendercharacters,
			  'renderopticallens':renderopticallens,
			  
			  #SFX
			  'renderlightiningsfx': renderlightiningsfx,    
			  'renderenvironmentalsfx': renderenvironmentalsfx,  
			  'renderweaponsfx':renderweaponsfx,    
			  'renderfiresfx': renderfiresfx,  
			  'renderenergysfx': renderenergysfx,    
			  'renderfightiningsfx':renderfightiningsfx,  
			  'rendermachinerysfx':rendermachinerysfx,  
						  
			  #VFX                                          
			  'renderlightiningvfx': renderlightiningvfx,                 
			  'renderenergyvfx':renderenergyvfx, 
			  'rendermuzzleflashesvfx':rendermuzzleflashesvfx,
			  'rendershockwavesvfx':rendershockwavesvfx ,  
			  'renderparticlevfx':renderparticlevfx,
			   'renderenvironmentalvfx':renderenvironmentalvfx,   
			   'renderdebrisandcrackvfx': renderdebrisandcrackvfx,
						 
			  'order': order,
			  'TotalCartAmount':TotalCartAmount, 
			  'TotalCartItems': TotalCartItems,

			  }
	return render(request, 'E-HUB/cart.html', context)#for displaying no of item in red circle of cart icon 

@login_required(login_url='login')
def DownloadProducts(request):
	if request.user.is_authenticated:
		customer=request.user.customer
		purchasedaudiospectrums={}
		purchasedlyricstemplates={}                
		
 #If the order is not completed and customer visit downloadpage send empty dictionary so error wouldnot generate        
		
	#SpecialPacks    
		purchasedaudiopacks={}
		purchasedvfxpack={}
		purchasedflimtransitionpack={}     
		purchasedmotiongraphicspack={}
		
	#Graphics elements    
		purchasedlandscapes={}
		purchasedcharacters={}
		purchasedopticallens={}
		
	#Sfx    
		purchasedlightiningsfx={}
		purchasedenvironmentalsfx={}
		purchasedweaponsfx={}
		purchasedfiresfx={}     
		purchasedenergysfx={}
		purchasedfightiningsfx={}
		purchasedmachinerysfx={}
	
	#Vfx    
		purchasedlightiningvfx={}
		purchasedenergyvfx={}
		purchasedmuzzleflashesvfx={}
		purchasedshockwavesvfx={}     
		purchasedparticlevfx={}
		purchasedenvironmentalvfx={}
		purchaseddebrisandcrackvfx={}     
		
		
		for i in PurchasedProducts.objects.filter(customer=customer,complete=True):
			#OTHERS
			purchasedaudiospectrums = i.orderaudiospectrum_set.all()
			purchasedlyricstemplates=i.orderlyricstemplates_set.all()
			
			#SPECIALPACKS
			purchasedaudiopacks=i.ordersoundpack_set.all()
			purchasedvfxpack=i.ordervfxpack_set.all()
			purchasedflimtransitionpack=i.orderflimtransition_set.all()        
			purchasedmotiongraphicspack=i.ordermotiongraphicspack_set.all()
			
			
			#GRAPHICS ELEMENTS
			purchasedlandscapes=i.orderlandscape_set.all()
			purchasedcharacters=i.ordercharacter_set.all()    
			purchasedopticallens=i.orderopticallense_set.all()           
			#SFX
			purchasedlightiningsfx=i.orderlightiningsfx_set.all()
			purchasedenvironmentalsfx=i.orderenvironmentalsfx_set.all()        
			purchasedfiresfx=i.orderfiresfx_set.all()
			purchasedenergysfx=i.orderenergysfx_set.all()    
			purchasedfightiningsfx=i.orderfightingsfx_set.all()        
			purchasedweaponsfx=i.orderweaponssfx_set.all()
			purchasedmachinerysfx=i.ordermachinerysfx_set.all()              
				
			#VFX
			purchasedenergyvfx=i.orderenergyvfx_set.all()
			purchasedlightiningvfx=i.orderlightiningvfx_set.all()    
			purchasedmuzzleflashesvfx=i.ordermuzzleflashesvfx_set.all()
			purchasedshockwavesvfx=i.ordershockwavesvfx_set.all()   
			purchasedparticlevfx=i.orderparticlevfx_set.all()
			purchasedenvironmentalvfx=i.orderenvironmentalvfx_set.all() 
			purchaseddebrisandcrackvfx=i.orderdebrisandcracksvfx_set.all()
	  
		context = { 
						#Others
				'purchasedaudiospectrums':purchasedaudiospectrums,
				'purchasedlyricstemplates':purchasedlyricstemplates,
				
				#SpecialPacks
				'purchasedaudiopacks': purchasedaudiopacks,
				'purchasedvfxpack':purchasedvfxpack,
				'purchasedflimtransitionpack':purchasedflimtransitionpack,
				'purchasedmotiongraphicspack':purchasedmotiongraphicspack  ,                  
				
				#GRAPHICS ELEMENTS
				'purchasedlandscapes': purchasedlandscapes,
				'purchasedcharacters': purchasedcharacters,
				'purchasedopticallens':purchasedopticallens,
				
				#SFX
				'purchasedlightiningsfx': purchasedlightiningsfx,    
				'purchasedenvironmentalsfx': purchasedenvironmentalsfx,  
				'purchasedweaponsfx':purchasedweaponsfx,    
				'purchasedfiresfx': purchasedfiresfx,  
				'purchasedenergysfx': purchasedenergysfx,    
				'purchasedfightiningsfx':purchasedfightiningsfx,  
				'purchasedmachinerysfx':purchasedmachinerysfx,  
							
				#VFX                                          
				'purchasedlightiningvfx': purchasedlightiningvfx,                 
				'purchasedenergyvfx':purchasedenergyvfx, 
				'purchasedmuzzleflashesvfx':purchasedmuzzleflashesvfx,
				'purchasedshockwavesvfx':purchasedshockwavesvfx ,  
				'purchasedparticlevfx':purchasedparticlevfx,
				'purchasedenvironmentalvfx':purchasedenvironmentalvfx,   
				'purchaseddebrisandcrackvfx': purchaseddebrisandcrackvfx,
		
				}                

	return render(request,'E-HUB/downloadpage.html', context)
	
@login_required(login_url='login')    
def Checkout(request):  
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)  #we are setting the customer value on authebnticating the user
		
		#OTHERS
		renderaudiospectrums = order.orderaudiospectrum_set.all()
		renderlyricstemplates = order.orderlyricstemplates_set.all()    
		
		#SPECIALPACKS
		renderaudiopack=order.ordersoundpack_set.all()
		rendervfxpack=order.ordervfxpack_set.all()
		renderflimtransitionpack=order.orderflimtransition_set.all()        
		rendermotiongraphicspack=order.ordermotiongraphicspack_set.all()
				
		#GRAPHICS ELEMENTS
		renderlandscapes = order.orderlandscape_set.all()   
		rendercharacters=order.ordercharacter_set.all()
		renderopticallens = order.orderopticallense_set.all()  
		
		#SFX
		renderlightiningsfx=order.orderlightiningsfx_set.all()
		renderenvironmentalsfx=order.orderenvironmentalsfx_set.all()        
		renderfiresfx=order.orderfiresfx_set.all()
		renderenergysfx=order.orderenergysfx_set.all()    
		renderfightiningsfx=order.orderfightingsfx_set.all()        
		renderweaponsfx=order.orderweaponssfx_set.all()
		rendermachinerysfx=order.ordermachinerysfx_set.all()              
			 
		#VFX
		renderenergyvfx=order.orderenergyvfx_set.all()
		renderlightiningvfx=order.orderlightiningvfx_set.all()    
		rendermuzzleflashesvfx=order.ordermuzzleflashesvfx_set.all()
		rendershockwavesvfx=order.ordershockwavesvfx_set.all()   
		renderparticlevfx=order.orderparticlevfx_set.all()
		renderenvironmentalvfx=order.orderenvironmentalvfx_set.all() 
		renderdebrisandcrackvfx=order.orderdebrisandcracksvfx_set.all()        

		TotalCartAmount=order.get_lightiningvfx_total+order.get_energyvfx_total+order.get_muzzleflashes_total+order.get_shockwaves_total+order.get_particles_total+order.get_environmentvfx_total+order.get_debrisandcracksvfx_total+order.get_lightiningsfx_total+order.get_energysfx_total+order.get_environmentalsfx_total+order.get_firesfx_total+order.get_machinerysfx_total+order.get_weaponsfx_total+order.get_fightingsfx_total+order.get_landscapes_total+order.get_characters_total+order.get_opticallens_total+order.get_audiopack_total+order.get_vfxpack_total+order.get_flimtransitionpack_total+order.get_motiongraphicspack_total+order.get_audiospectrum_total+order.get_lyricstemplate_total
		TotalCartItems=order.get_lightiningvfx_items+order.get_energyvfx_items+order.get_muzzleflashes_items+order.get_shockwaves_items+order.get_particles_items+order.get_environmentvfx_items+order.get_debrisandcracksvfx_items+order.get_lightiningsfx_items+order.get_energysfx_items+order.get_environmentalsfx_items+order.get_firesfx_items+order.get_machinerysfx_items+order.get_weaponsfx_items+order.get_fightingsfx_items+order.get_landscapes_items+order.get_characters_items+order.get_opticallens_items+order.get_audiopack_items+order.get_vfxpack_items+order.get_flimtransitionpack_items+order.get_motiongraphicspack_items+order.get_audiospectrum_items+order.get_lyricstemplate_items
	   
	else:
		cartItems=0
		items = []
		order = {'get_cart_total': 0, 'get_cart_items': 0 ,'shipping':False }
		
	context = {
			  #Others
			  'renderaudiospectrums':renderaudiospectrums,
			  'renderlyricstemplates':renderlyricstemplates,
			  
			  #SpecialPacks
			  'renderaudiopack': renderaudiopack,
			  'rendervfxpack':rendervfxpack,
			  'renderflimtransitionpack':renderflimtransitionpack,
			  'rendermotiongraphicspack':rendermotiongraphicspack,
			  
			  #GRAPHICS ELEMENTS
			  'renderlandscapes':renderlandscapes,       
			  'rendercharacters':rendercharacters,
			  'renderopticallens':renderopticallens,   
			  
			  #SFX
			  'renderlightiningsfx': renderlightiningsfx,    
			  'renderenvironmentalsfx': renderenvironmentalsfx,  
			  'renderweaponsfx':renderweaponsfx,    
			  'renderfiresfx': renderfiresfx,  
			  'renderenergysfx': renderenergysfx,    
			  'renderfightiningsfx':renderfightiningsfx,  
			  'rendermachinerysfx':rendermachinerysfx,  
						  
			  #VFX                                          
			  'renderlightiningvfx': renderlightiningvfx,                 
			  'renderenergyvfx':renderenergyvfx, 
			  'rendermuzzleflashesvfx':rendermuzzleflashesvfx,
			  'rendershockwavesvfx':rendershockwavesvfx ,  
			  'renderparticlevfx':renderparticlevfx,
			   'renderenvironmentalvfx':renderenvironmentalvfx,   
			   'renderdebrisandcrackvfx': renderdebrisandcrackvfx,

			   'TotalCartAmount':TotalCartAmount,
			   'TotalCartItems':TotalCartItems,

			   'order': order,

			   }
	
	return render(request, 'E-HUB/checkout.html', context)

class KhaltiVerifyView(View):
	print('Initaiting Khalti Verificatiion...')
	def get(self, request, *args, **kwargs):
		transaction_id = datetime.datetime.now().timestamp()
		
		token = request.GET.get("token")
		amount = request.GET.get("amount")
		o_id = request.GET.get("order_id")
		customer=request.user.customer
		print(o_id)
		print(token, amount, o_id)

		url = "https://khalti.com/api/v2/payment/verify/"
		payload = {
			"token": token,
			"amount": amount
		}
		headers = {
			"Authorization": "Key test_secret_key_de01b0c1f02b48759df0953a0dcfc8f0"
		}

		order = Order.objects.get(customer=customer,id=o_id,complete=False)
		purchase= PurchasedProducts.objects.get(customer=customer, complete=False)  
		TotalCartAmount=order.get_lightiningvfx_total+order.get_energyvfx_total+order.get_muzzleflashes_total+order.get_shockwaves_total+order.get_particles_total+order.get_environmentvfx_total+order.get_debrisandcracksvfx_total+order.get_lightiningsfx_total+order.get_energysfx_total+order.get_environmentalsfx_total+order.get_firesfx_total+order.get_machinerysfx_total+order.get_weaponsfx_total+order.get_fightingsfx_total+order.get_landscapes_total+order.get_characters_total+order.get_opticallens_total+order.get_audiopack_total+order.get_vfxpack_total+order.get_flimtransitionpack_total+order.get_motiongraphicspack_total+order.get_audiospectrum_total+order.get_lyricstemplate_total      
		
		response = requests.post(url, payload, headers=headers)#sending data to url
		resp_dict = response.json()
		print(resp_dict.get('idx'))
		
		total=amount
		if resp_dict.get("idx"):
			if total ==amount:
					success = True
					order.complete= True
					order.transaction_id = transaction_id 
					order.save()
					
					purchase.complete= True
					purchase.transaction_id = transaction_id 
					purchase.save()      
					
					orderenergyvfx = OrderEnergyVfx.objects.filter(customer=customer,complete=False)#get all the energyvfx item from the database whose complete status is false.
					orderlightiningvfx = OrderLightiningVfx.objects.filter(customer=customer,complete=False)
					ordermuzzleflashes = OrderMuzzleflashesVfx.objects.filter(customer=customer,complete=False)
					ordershockwaves = OrderShockwavesVfx.objects.filter(customer=customer,complete=False)
					orderparticlevfx = OrderParticleVfx.objects.filter(customer=customer,complete=False)
					orderenvironmentalvfx=OrderEnvironmentalVfx.objects.filter(customer=customer,complete=False)
					orderdebrisandcrackvfx=OrderDebrisAndCracksVfx.objects.filter(customer=customer,complete=False)
					
					orderlightiningsfx = OrderLightiningSfx.objects.filter(customer=customer,complete=False)
					orderenvironmentalsfx = OrderEnvironmentalSfx.objects.filter(customer=customer,complete=False)        
					orderfiresfx = OrderFireSfx.objects.filter(customer=customer,complete=False)
					ordermachinerysfx = OrderMachinerySfx.objects.filter(customer=customer,complete=False)
					orderenergysfx=OrderEnergySfx.objects.filter(customer=customer,complete=False)
					orderweaponsfx=OrderWeaponsSfx.objects.filter(customer=customer,complete=False)
					orderfightingsfx=OrderFightingSfx.objects.filter(customer=customer,complete=False)
					
					ordersoundpack = OrderSoundPack.objects.filter(customer=customer,complete=False)
					ordervfxpack = OrderVfxPack.objects.filter(customer=customer,complete=False)
					orderflimtransitionpack=OrderFlimTransition.objects.filter(customer=customer,complete=False)
					ordermotiongraphicspack=OrderMotionGraphicsPack.objects.filter(customer=customer,complete=False)       
							
					ordercharacter=OrderCharacter.objects.filter(customer=customer,complete=False)
					orderlandscape=OrderLandscape.objects.filter(customer=customer,complete=False)
					orderopticallens=OrderOpticalLense.objects.filter(customer=customer,complete=False)


			#VFX          
					for x in orderenergyvfx:
						x.complete = True  
						x.save()
						
					for x in orderlightiningvfx:
						x.complete = True  
						x.save()   
				
					for x in ordermuzzleflashes:
						x.complete = True  
						x.save()
						
					for x in ordershockwaves:
						x.complete = True  
						x.save()    
					
					for x in orderparticlevfx:

						x.complete = True  
						x.save()
						
					for x in orderenvironmentalvfx:
						x.complete = True  
						x.save()    
				
					for x in orderdebrisandcrackvfx:

						x.complete = True  
						x.save()                                                 
					
			#SFX
					for x in orderlightiningsfx:
						x.complete = True  
						x.save()
					
					for x in orderenvironmentalsfx:
						x.complete = True  
						x.save()
				
					for x in orderfiresfx:
						x.complete = True  
						x.save()
					
					for x in ordermachinerysfx:
						x.complete = True  
						x.save()                               
					
					for x in orderenergysfx:
						x.complete = True  
						x.save()
						
					for x in orderweaponsfx:
						x.complete = True  
						x.save() 
					
					for x in orderfightingsfx:
						x.complete = True  
						x.save()
						
					#SPECIAL PACKS
					for x in ordersoundpack:
						x.complete = True  
						x.save()                           
					
					for x in ordervfxpack:
						x.complete = True  
						x.save()
						
					for x in orderflimtransitionpack:
						x.complete = True  
						x.save()
					
					for x in ordermotiongraphicspack:
						x.complete = True  
						x.save()                                    
					
					#GRAPHICS ELEMENT   
					for x in ordercharacter:
						x.complete = True  
						x.save()
						
					for x in orderlandscape:
						x.complete = True  
						x.save()         
						
					for x in orderopticallens:
						x.complete = True  
						x.save()
										  
			else:
				success = False
			data = {
				"success": success
			}
			return JsonResponse(data)
   
def ProcessOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)  #parsing data for acessing it

	if request.user.is_authenticated:
		customer = request.user.customer
		total = float(data['form']['total'])  #we are accessing total amount from form object
		
		#For clearing Cart
		order = Order.objects.get(customer=customer, complete=False)
		#For downloading items that are completed of particular Customer
		purchase= PurchasedProducts.objects.get(customer=customer, complete=False)    
					 
		order.transaction_id = transaction_id 
		purchase.transaction_id = transaction_id
		TotalCartAmount=order.get_lightiningvfx_total+order.get_energyvfx_total+order.get_muzzleflashes_total+order.get_shockwaves_total+order.get_particles_total+order.get_environmentvfx_total+order.get_debrisandcracksvfx_total+order.get_lightiningsfx_total+order.get_energysfx_total+order.get_environmentalsfx_total+order.get_firesfx_total+order.get_machinerysfx_total+order.get_weaponsfx_total+order.get_fightingsfx_total+order.get_landscapes_total+order.get_characters_total+order.get_opticallens_total+order.get_audiopack_total+order.get_vfxpack_total+order.get_flimtransitionpack_total+order.get_motiongraphicspack_total+order.get_audiospectrum_total+order.get_lyricstemplate_total
		
		if total == float(TotalCartAmount):
			order.complete = True  
		order.save()
		
		if purchase.complete==False:
			if purchase.customer==customer:
				purchase.complete=True
			purchase.save()  
						  
		#When the payment is completed,set all the order items to True of the logged in user only not others.
		#Note,We dont need to mention publisher_Id    
		orderenergyvfx = OrderEnergyVfx.objects.filter(customer=customer,complete=False)#get all the energyvfx item from the database whose complete status is false.
		orderlightiningvfx = OrderLightiningVfx.objects.filter(customer=customer,complete=False)
		ordermuzzleflashes = OrderMuzzleflashesVfx.objects.filter(customer=customer,complete=False)
		ordershockwaves = OrderShockwavesVfx.objects.filter(customer=customer,complete=False)
		orderparticlevfx = OrderParticleVfx.objects.filter(customer=customer,complete=False)
		orderenvironmentalvfx=OrderEnvironmentalVfx.objects.filter(customer=customer,complete=False)
		orderdebrisandcrackvfx=OrderDebrisAndCracksVfx.objects.filter(customer=customer,complete=False)
		
		orderlightiningsfx = OrderLightiningSfx.objects.filter(customer=customer,complete=False)
		orderenvironmentalsfx = OrderEnvironmentalSfx.objects.filter(customer=customer,complete=False)        
		orderfiresfx = OrderFireSfx.objects.filter(customer=customer,complete=False)
		ordermachinerysfx = OrderMachinerySfx.objects.filter(customer=customer,complete=False)
		orderenergysfx=OrderEnergySfx.objects.filter(customer=customer,complete=False)
		orderweaponsfx=OrderWeaponsSfx.objects.filter(customer=customer,complete=False)
		orderfightingsfx=OrderFightingSfx.objects.filter(customer=customer,complete=False)
		
		ordersoundpack = OrderSoundPack.objects.filter(customer=customer,complete=False)
		ordervfxpack = OrderVfxPack.objects.filter(customer=customer,complete=False)
		orderflimtransitionpack=OrderFlimTransition.objects.filter(customer=customer,complete=False)
		ordermotiongraphicspack=OrderMotionGraphicsPack.objects.filter(customer=customer,complete=False)       
				
		ordercharacter=OrderCharacter.objects.filter(customer=customer,complete=False)
		orderlandscape=OrderLandscape.objects.filter(customer=customer,complete=False)
		orderopticallens=OrderOpticalLense.objects.filter(customer=customer,complete=False)


  #VFX          
		for x in orderenergyvfx:
			if total == float(TotalCartAmount):
				x.complete = True  
			x.save()
			
		for x in orderlightiningvfx:
			if total == float(TotalCartAmount):
				x.complete = True  
			x.save()   
	   
		for x in ordermuzzleflashes:
			if total == float(TotalCartAmount):
				x.complete = True  
			x.save()
			
		for x in ordershockwaves:
			if total == float(TotalCartAmount):
				x.complete = True  
			x.save()    
		   
		for x in orderparticlevfx:
			if total == float(TotalCartAmount):
				x.complete = True  
			x.save()
			
		for x in orderenvironmentalvfx:
			if total == float(TotalCartAmount):
				x.complete = True  
			x.save()    
	  
		for x in orderdebrisandcrackvfx:
			if total == float(TotalCartAmount):
				x.complete = True  
			x.save()                                                 
		 
 #SFX
		for x in orderlightiningsfx:
			if total == float(TotalCartAmount):
				x.complete = True  
			x.save()
		 
		for x in orderenvironmentalsfx:
			if total == float(TotalCartAmount):
				x.complete = True  
			x.save()
	   
		for x in orderfiresfx:
			if total == float(TotalCartAmount):
				x.complete = True  
			x.save()
		  
		for x in ordermachinerysfx:
			if total == float(TotalCartAmount):
				x.complete = True  
			x.save()                                    
		 
		for x in orderenergysfx:
			if total == float(TotalCartAmount):
				x.complete = True  
			x.save()    
			
		for x in orderweaponsfx:
			if total == float(TotalCartAmount):
				x.complete = True  
			x.save()     
		   
		for x in orderfightingsfx:
			if total == float(TotalCartAmount):
				x.complete = True  
			x.save()  
			
		#SPECIAL PACKS
		for x in ordersoundpack:
			if total == float(TotalCartAmount):
				x.complete = True  
			x.save()                                    
		 
		for x in ordervfxpack:
			if total == float(TotalCartAmount):
				x.complete = True  
			x.save()    
			
		for x in orderflimtransitionpack:
			if total == float(TotalCartAmount):
				x.complete = True  
			x.save()     
		   
		for x in ordermotiongraphicspack:
			if total == float(TotalCartAmount):
				x.complete = True  
			x.save()                                       
		 
		 #GRAPHICS ELEMENT   
		for x in ordercharacter:
			if total == float(TotalCartAmount):
				x.complete = True  
			x.save()
			
		for x in orderlandscape:
			if total == float(TotalCartAmount):
				x.complete = True  
			x.save()         
			
		for x in orderopticallens:
			if total == float(TotalCartAmount):
				x.complete = True  
			x.save()                 
					
	else:
		print('User not logged in')

	return JsonResponse('Payment Completed', safe=False)    #console.log('Sucess:', data);

#REGISTRATION AND LOGIN SECTION
def loginuser(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user_obj = User.objects.filter(username = username).first()
		if user_obj is None:
			messages.error(request, 'User not found.')
			return redirect('login')
		
		
		customer_obj = Customer.objects.filter(user = user_obj ).first()

		if not customer_obj.is_verified:
			messages.error(request, 'Your account is not verified yet .Check your mail.')
			return redirect('login')

		user = authenticate(username = username , password = password)
		if user is None:
			messages.error(request, 'Wrong password.')
			return redirect('login')
		
		login(request , user)
		return redirect('home')

	return render(request , 'Sign-Up/login.html')

def logoutUser(request):
	logout(request)
	return redirect('home')     

def register(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		email = request.POST.get('email')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')

		try:
			#checking if the new one is using the same username or email
			if User.objects.filter(username = username).first():
				messages.error(request, 'Username is taken.')
				return redirect('register')

			if User.objects.filter(email = email).first():
				messages.error(request, 'Email is taken.')
				return redirect('register')
			

			if password1 == password2:
								#create user  and saving it
				user_obj = User(username = username , email = email)
				user_obj.set_password(password1)
				user_obj.save()
				
				#When User clicks on SignIn 
				# 1.we are generating an token and creating a profile based on the auth_token that was generated.
				#2.sending the email through a function with email and auth_token as a paramter
				auth_token = str(uuid.uuid4())#converting to string
				custom_obj = Customer.objects.create(user = user_obj ,email=email ,auth_token = auth_token)
				custom_obj.save()
				
				#Now, We are sending the auth_token that was generated by uuid to gmail.We make a function.
				send_mail_after_registration(email , auth_token)  #function call
				return redirect('token_send')
			else:
				 messages.error(request, 'Sorry,Password1 and Password2 did not match.')
				

		except Exception as e:
			print(e)

	return render(request , 'Sign-Up/registration.html')

def success(request):
	return render(request , 'Sign-Up/success.html')

def token_send(request):
	return render(request , 'Sign-Up/token_send.html')

def verify(request , auth_token):
	try:
		customer_obj = Customer.objects.filter(auth_token = auth_token).first() #checking if the profile exist through auth_token
	
		if customer_obj:#if profile exists
			
			if customer_obj.is_verified:#If the profile that exists has already been verified return User to login page
				messages.success(request, 'Your account is already verified.')
				return redirect('login')
			
			#If profile exists set the is_verified to True, save it and redirect to login page
			customer_obj.is_verified = True
			customer_obj.save()
			messages.success(request, 'Your account has been verified.')
			return redirect('login')
		
		#if the profile with the passed auth_token doesn;t exist throw error
		else:
			return redirect('error')
	except Exception as e:
		print(e)
		return redirect('/')
	

def error_page(request):
	return  render(request , 'Sign-Up/error.html')


def send_mail_after_registration(email , token):
	subject = 'Your DI account need to be verified.'
	message = f'Dear Sir/Madam paste the link to verify your DI account http://dimensionalillusions.herokuapp.com/account/verify/{token}'
	#message = f'Dear Sir/Madam paste the link to verify your DI account http://127.0.0.1:8000/account/verify/{token}'
	email_from = settings.EMAIL_HOST_USER
	recipient_list = [email]#from args
	send_mail(subject, message , email_from ,recipient_list )#a function that sends a email to gmail
	