from django.shortcuts import render
from VFX.models import *
from SFX.models import *
from OTHERS.models import *
from GraphicsElements.models import *
from SpecialPacks.models import *
from EHub.decorators import *
from django.utils import timezone

from .forms import *

from django.contrib.auth.decorators import login_required  #Restriciton ofp Pages (For not to display pages for anonymous user(but only logged in users))
from django.contrib import messages


# Create your views here.
 #This Decorator is taking this dashboard function inside it
@login_required(login_url='login') 
@allowed_users(allowed_roles=['Admin','Graphics Manager'])
def dashboard(request):
    context={}
    if request.user.is_authenticated:
        customer=request.user
        custom = str(request.user.customer)
        print(customer.id)
        #Render Data based on name of User    
        currentlocaltime = timezone.now()
        context={
                        'currentlocaltime':currentlocaltime,
         }          
        if customer.groups.filter(name="Graphics Manager").exists():

         #Orders Completed
                #count all the landscape ordered  by customers which was published by Pub Id in website.
                CountCompletedOrderedLandscapes=OrderLandscape.objects.filter(published_by=customer,complete=True).count()
                CountCompletedOrderedCharacters=OrderCharacter.objects.filter(published_by=customer,complete=True).count()
                OrdersCompleted=CountCompletedOrderedLandscapes+CountCompletedOrderedCharacters
                
            #Orders Pending    
                CountInCompletedOrderedLandscapes=OrderLandscape.objects.filter(published_by=customer,complete=False).count()
                CountInCompletedOrderedCharacters=OrderCharacter.objects.filter(published_by=customer,complete=False).count()
                OrdersPending=CountInCompletedOrderedLandscapes+CountInCompletedOrderedCharacters

                print(OrdersPending)
                print(CountInCompletedOrderedLandscapes)
                
            #Your Orders    
                LandscapesOrders=OrderLandscape.objects.filter(published_by=customer)
                CharactersOrders=OrderCharacter.objects.filter(published_by=customer)
        
            #Earnings Setup
                TotalLandscapePrice=0
                for x in OrderLandscape.objects.filter(published_by=customer,complete=True):
                    pprice=x.product.price
                    chargedprice=float(pprice)-10/100*float(pprice) #10%charge from me
                    TotalLandscapePrice=TotalLandscapePrice+chargedprice
                print(TotalLandscapePrice)      

                TotalCharacterPrice=0
                for x in OrderCharacter.objects.filter(published_by=customer,complete=True):
                    pprice=x.product.price
                    chargedprice=float(pprice)-10/100*float(pprice) #10%charge from me
                    TotalCharacterPrice=TotalCharacterPrice+chargedprice
                print(TotalCharacterPrice)      				
                    
                MyEarnings=TotalLandscapePrice+TotalCharacterPrice
                print(MyEarnings)
                
                context = {
                    'currentlocaltime':currentlocaltime,
                    'OrdersCompleted':OrdersCompleted,
                    'OrdersPending': OrdersPending,        
                    'LandscapesOrders':LandscapesOrders,
                    'CharactersOrders':CharactersOrders,
                    'MyEarnings':MyEarnings,
                    'customer':customer,
                    }   
                
     
    else:
         context={
         }
            
    return render(request,'dashboard/dashbase.html',context)

@login_required(login_url='login') 
@allowed_users(allowed_roles=['Admin','Graphics Manager'])
def profileinfo(request,pk):
    if request.user.is_authenticated:
        currentlocaltime = timezone.now()
        
        custominfo=Customer.objects.get(id=pk)
        customid=custominfo.id
        print(customid)
        
        profileform=ProfileForm(instance=custominfo)
     
        if request.method=="POST":
            profileform=ProfileForm(request.POST,request.FILES,instance=custominfo)
            if profileform.is_valid():
                profileform.save()
                return redirect('/account/dashboard/profiledetail/'+pk)        
            
        context = {
            'profileform':profileform,
            'currentlocaltime':currentlocaltime,

            'customid':customid,
            }   
    
    else:
         context={}
            
    return render(request,'dashboard/profileinfo.html',context)
 
@login_required(login_url='login') 
@allowed_users(allowed_roles=['Admin']) 
def energy(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        user=request.user
        currentlocaltime = timezone.now()
        #check if user falls under the graphics manager grant his products
        if user.groups.filter(name="Admin").exists():
           getenergies=EnergyVfx.objects.filter(publisher=customer)
           getelectricites=LightiningVfx.objects.filter(publisher=customer)
           context={
                          'getenergies':getenergies,
                          'getelectricites':getelectricites,
                          'currentlocaltime':currentlocaltime,
           }
    return render(request,'dashboard/energy/energy.html',context) 
 
@login_required(login_url='login') 
@allowed_users(allowed_roles=['Admin']) 
def addenergy(request):
    energyform=EnergyVfxForm()
    getpublisher=request.user.customer
    print(getpublisher)
    currentlocaltime = timezone.now()
    if request.method=="POST":
            energyform=EnergyVfxForm(request.POST,request.FILES)
            if energyform.is_valid():
                newform=energyform.save()
                newform.publisher=getpublisher
                print(newform)
                newform.save()
                return redirect('energy')

    context={
            'energyform':energyform,
            'currentlocaltime':currentlocaltime,
    }
    return render(request,'dashboard/energy/addenergy.html',context) 

@login_required(login_url='login') 
@allowed_users(allowed_roles=['Admin']) 
def updateenergy(request,pk):
    energyvfx=EnergyVfx.objects.get(id=pk)
    energyform=EnergyVfxForm(instance=energyvfx)
    currentlocaltime = timezone.now()

    if request.method=="POST":
            energyform=EnergyVfxForm(request.POST,request.FILES,instance=energyvfx)
            if energyform.is_valid():
                energyform.save()
                return redirect('energy')

    context={
            'energyform':energyform,
            'currentlocaltime':currentlocaltime,
        
    }
    return render(request,'dashboard/energy/updateenergy.html',context) 

@login_required(login_url='login') 
@allowed_users(allowed_roles=['Admin']) 
def deleteenergy(request,pk):
    energyvfx=EnergyVfx.objects.get(id=pk)
    currentlocaltime = timezone.now()
    if request.method=="POST":
       energyvfx.delete()
       return redirect('energy')
    context={
            'item':energyvfx,
            'currentlocaltime':currentlocaltime,
        
    }
    return render(request,'dashboard/energy/deleteenergy.html',context) 


#LANDSCAPE CRUD
@login_required(login_url='login') 
@allowed_users(allowed_roles=['Graphics Manager']) 
def landscape(request):
    if request.user.is_authenticated:
        currentlocaltime = timezone.now()
     #note everytime we create a user customer is also created with same name
        customer=request.user.customer
        user=request.user
     
        #check if user falls under the graphics manager grant his products
        if user.groups.filter(name="Graphics Manager").exists():
           getlandscapes=Landscapes.objects.filter(publisher=customer)
           context={
                          'getlandscapes':getlandscapes,
                          'currentlocaltime':currentlocaltime,

           }	

    return render(request,'dashboard/landscape/landscapes.html',context) 
 
@login_required(login_url='login') 

#check if user falls under the graphics manager grant premission to add Graphics
@allowed_users(allowed_roles=['Graphics Manager']) 
def addlandscape(request):
    landscapeform= LandscapeForm()
    getpublisher=request.user.customer
    currentlocaltime = timezone.now()
    if request.method=="POST":
            landscapeform=LandscapeForm(request.POST,request.FILES)
            if landscapeform.is_valid():
                newform=landscapeform.save()
                newform.publisher=getpublisher
                newform.save()
                landscapeform.save()
                return redirect('landscape')

    context={
            'landscapeform':landscapeform,
            'currentlocaltime':currentlocaltime,
        
    }
    return render(request,'dashboard/landscape/addlandscape.html',context) 

@login_required(login_url='login') 
@allowed_users(allowed_roles=['Graphics Manager']) 
def updatelandscape(request,pk):
    landscape=Landscapes.objects.get(id=pk)
    landscapeform= LandscapeForm(instance=landscape)
    currentlocaltime = timezone.now()

    if request.method=="POST":
            landscapeform=LandscapeForm(request.POST,request.FILES,instance=landscape)
            if landscapeform.is_valid():
                landscapeform.save()
                return redirect('landscape')

    context={
            'landscapeform':landscapeform,
            'currentlocaltime':currentlocaltime,
        
    }
    return render(request,'dashboard/landscape/updatelandscape.html',context) 

@login_required(login_url='login') 
@allowed_users(allowed_roles=['Graphics Manager']) 
def deletelandscape(request,pk):
    landscape=Landscapes.objects.get(id=pk) 
    currentlocaltime = timezone.now()
    if request.method=="POST":
       landscape.delete()
       return redirect('landscape')
    context={
            'item':landscape,
            'currentlocaltime':currentlocaltime,
        
    }
    return render(request,'dashboard/landscape/deletelandscape.html',context)     

#CHARACTER CRUD
@login_required(login_url='login') 
@allowed_users(allowed_roles=['Graphics Manager']) 
def character(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        user=request.user
        currentlocaltime = timezone.now()
     
        if user.groups.filter(name="Graphics Manager").exists():
           getcharacters=Characters.objects.filter(publisher=customer)
           context={
                          'getcharacters':getcharacters,
                          'currentlocaltime':currentlocaltime,
           }			   	   
    return render(request,'dashboard/character/characters.html',context) 
 
@login_required(login_url='login') 
@allowed_users(allowed_roles=['Graphics Manager']) 
def addcharacter(request):
    characterform= CharacterForm()
    getpublisher=request.user.customer
    currentlocaltime = timezone.now()
    if request.method=="POST":
            characterform=CharacterForm(request.POST,request.FILES)
            if characterform.is_valid():
                newform=characterform.save()
                newform.publisher=getpublisher
                characterform.save()
                return redirect('character')
    context={
             'characterform':characterform,
             'currentlocaltime':currentlocaltime,
    }
    return render(request,'dashboard/character/addcharacter.html',context) 

@login_required(login_url='login') 
@allowed_users(allowed_roles=['Graphics Manager']) 
def updatecharacter(request,pk):
    character=Characters.objects.get(id=pk)
    characterform= CharacterForm(instance=character)
    currentlocaltime = timezone.now()
    if request.method=="POST":
            characterform=CharacterForm(request.POST,request.FILES,instance=character)
            if characterform.is_valid():
                characterform.save()
                return redirect('character')

    context={
            'characterform':characterform,
            'currentlocaltime':currentlocaltime,
        
    }
    return render(request,'dashboard/character/updatecharacter.html',context) 

@login_required(login_url='login') 
@allowed_users(allowed_roles=['Graphics Manager']) 
def deletecharacter(request,pk):
    character=Characters.objects.get(id=pk)
    currentlocaltime = timezone.now()
    if request.method=="POST":
       character.delete()
       return redirect('character')
    context={
            'item':character,
            'currentlocaltime':currentlocaltime,
        
    }
    return render(request,'dashboard/character/deletecharacter.html',context)     
