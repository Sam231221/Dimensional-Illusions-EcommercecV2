from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import FileExtensionValidator,MinValueValidator,MaxValueValidator

# Create your models here.
class Customer(models.Model):  #Customer class is gonna inherit from models.Model  #customer is needed for certain user otherwise store.html wont work
    Gender_Choices=[
        ('Male','Male'),
        ('Female','Female'),
    ]  
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True) #cascade is for deleting the customer
    first_name = models.SlugField(max_length=10, null=True)
    second_name=models.CharField(max_length=10,null=True)
    
    email = models.EmailField(max_length=140, null=True,blank=True)
    image = models.ImageField(upload_to="thumbnails/profile/%y"
                              ,help_text="This will be uploaded as your profile picture. Only .png and .jpg are accepted"
                              ,validators=[FileExtensionValidator(['png','jpg'])]
                              ,blank=True,null=True)
    gender=models.CharField(choices=Gender_Choices,null=True,max_length=50)
    esewa_id=models.PositiveIntegerField(null=True
                                 ,help_text='This information will be used only for payment purpose.'
                                ,validators=[MinValueValidator(9400000000),MaxValueValidator(9999999999)]
                                 )
    auth_token = models.CharField(max_length=100,null=True)
    is_verified = models.BooleanField(default=False)        

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("profileinfo", kwargs={"pk": self.id,
                                                                      #"slug":self.first_name,
                                              })
     #kwargs={"pk":self.pk} pk is a must dont write id



'''
    Note in the frontend we have typed
                        <li class=""> <a class=" text-left " href="{{request.user.customer.get_absolute_url}}"
                            role="button" aria-haspopup="true" aria-expanded="false"><i
                                class="flaticon-bar-chart-1"></i> Account Details</a>
                    </li>
                    
                    We identified the customer through the request.user.customer and then get_absolute_url function is called.
                    This function automatically then gives us pk of that particular customer.It implements DRY principle
 '''   
    
        
class Contact(models.Model):
     sno= models.AutoField(primary_key=True)
     name= models.CharField(max_length=255)
     phone= models.CharField(max_length=13)
     email= models.EmailField(max_length=100)
     title= models.TextField(null=True)
     content= models.TextField(null=True)
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

     def __str__(self):
          return "Message from " + self.name + ' - ' + self.email

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)  #default is false which means unchecked box
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return "Ordered by "+str(self.customer)
 
 #VFX TOTALS
    @property  #meaning add property  see cart.html
    def get_lightiningvfx_total(self):  #get total value of all products with their respective quantity
        orderlightiningvfx = self.orderlightiningvfx_set.all()
        total = sum([item.get_total for item in orderlightiningvfx])
        return total

    @property
    def get_lightiningvfx_items(self):  #get total value of all products with their respective quantity
        orderlightiningvfx = self.orderlightiningvfx_set.all()
        total = sum([item.quantity for item in orderlightiningvfx])
        return total
    
    @property  #meaning add property  see cart.html
    def get_energyvfx_total(self):  #get total value of all products with their respective quantity
        orderenergiesvfx = self.orderenergyvfx_set.all()
        total = sum([item.get_total for item in orderenergiesvfx])
        return total

    @property
    def get_energyvfx_items(self):  #get items total
        orderenergiesvfx = self.orderenergyvfx_set.all()
        total = sum([item.quantity for item in orderenergiesvfx])
        return total
        
    @property  #meaning add property  see cart.html
    def get_muzzleflashes_total(self):  #get total value of all products with their respective quantity
        ordermuzzleflashes = self.ordermuzzleflashesvfx_set.all()
        total = sum([item.get_total for item in ordermuzzleflashes])
        return total

    @property  #meaning add property  see cart.html
    def get_muzzleflashes_items(self):  #get total value of all products with their respective quantity
        ordermuzzleflashes = self.ordermuzzleflashesvfx_set.all()
        total = sum([item.quantity for item in ordermuzzleflashes])
        return total
    
    @property  
    def get_shockwaves_total(self):  
        ordershockwaves = self.ordershockwavesvfx_set.all()
        total = sum([item.get_total for item in ordershockwaves])
        return total   

    @property  
    def get_shockwaves_items(self):  #
        ordershockwaves = self.ordershockwavesvfx_set.all()
        total = sum([item.quantity for item in ordershockwaves])
        return total       
    
    @property  
    def get_particles_total(self):  
        orderparticles = self.orderparticlevfx_set.all()
        total = sum([item.get_total for item in orderparticles])
        return total   

    @property  
    def get_particles_items(self):  #
        orderparticles = self.orderparticlevfx_set.all()
        total = sum([item.quantity for item in orderparticles])
        return total     
    
    @property  
    def get_environmentvfx_total(self):  
        orderenvironmentvfx = self.orderenvironmentalvfx_set.all()
        total = sum([item.get_total for item in orderenvironmentvfx])
        return total       
    
    @property  
    def get_environmentvfx_items(self):  
        orderenvironmentvfx = self.orderenvironmentalvfx_set.all()
        total = sum([item.quantity for item in orderenvironmentvfx])
        return total      
    
    @property  
    def get_debrisandcracksvfx_total(self):  
        orderdebrisandcracksvfx = self.orderdebrisandcracksvfx_set.all()
        total = sum([item.get_total for item in orderdebrisandcracksvfx])
        return total         
    
    @property  
    def get_debrisandcracksvfx_items(self):  
        orderdebrisandcracksvfx = self.orderdebrisandcracksvfx_set.all()
        total = sum([item.quantity for item in orderdebrisandcracksvfx])
        return total            
    
 #SFX TOTAL    
    @property  #meaning add property  see cart.html
    def get_lightiningsfx_total(self):  #get total price of all products related to EnergySfx with their respective quantity.
        orderlightiningsfx = self.orderlightiningsfx_set.all()
        total = sum([item.get_total for item in orderlightiningsfx])
        return total

    @property  #meaning add property  see cart.html
    def get_lightiningsfx_items(self):  #get total price of all products related to EnergySfx with their respective quantity.
        orderlightiningsfx = self.orderlightiningsfx_set.all()
        total = sum([item.quantity for item in orderlightiningsfx])
        return total
 
    @property  #meaning add property  see cart.html
    def get_environmentalsfx_total(self):  #get total price of all products related to EnergySfx with their respective quantity.
        orderenvironmentalsfx = self.orderenvironmentalsfx_set.all()
        total = sum([item.get_total for item in orderenvironmentalsfx])
        return total 
    
    @property  #meaning add property  see cart.html
    def get_environmentalsfx_items(self):  #get total price of all products related to EnergySfx with their respective quantity.
        orderenvironmentalsfx = self.orderenvironmentalsfx_set.all()
        total = sum([item.quantity for item in orderenvironmentalsfx])
        return total     
 
    @property  #meaning add property  see cart.html
    def get_firesfx_total(self):  #get total price of all products related to EnergySfx with their respective quantity.
        orderfiresfx = self.orderfiresfx_set.all()
        total = sum([item.get_total for item in orderfiresfx])
        return total

    @property
    def get_firesfx_items(self):  #get the total no of products related to EnergySfx
        orderfiresfx = self.orderfiresfx_set.all()
        total = sum([item.quantity for item in orderfiresfx])
        return total
 
    @property  #meaning add property  see cart.html
    def get_machinerysfx_total(self):  #get total price of all products related to EnergySfx with their respective quantity.
        ordermachinerysfx = self.ordermachinerysfx_set.all()
        total = sum([item.get_total for item in ordermachinerysfx])
        return total
    
    @property  #meaning add property  see cart.html
    def get_machinerysfx_items(self):  #get total price of all products related to EnergySfx with their respective quantity.
        ordermachinerysfx = self.ordermachinerysfx_set.all()
        total = sum([item.quantity for item in ordermachinerysfx])
        return total
    
    @property  #meaning add property  see cart.html
    def get_energysfx_total(self):  #get total price of all products related to EnergySfx with their respective quantity.
        orderenergysfx = self.orderenergysfx_set.all()
        total = sum([item.get_total for item in orderenergysfx])
        return total

    @property
    def get_energysfx_items(self):  #get the total no of products related to EnergySfx
        orderenergysfx = self.orderenergysfx_set.all()
        total = sum([item.quantity for item in orderenergysfx]) #sum up the no of quantity of each products related to EnergySfx  
        return total    
    
    @property
    def get_weaponsfx_total(self):  #get the total no of products related to EnergySfx
        orderweaponsfx = self.orderweaponssfx_set.all()
        total = sum([item.get_total for item in orderweaponsfx]) #sum up the no of quantity of each products related to EnergySfx  
        return total    
    
    @property
    def get_weaponsfx_items(self):  #get the total no of products related to EnergySfx
        orderweaponsfx = self.orderweaponssfx_set.all()
        total = sum([item.quantity for item in orderweaponsfx]) #sum up the no of quantity of each products related to EnergySfx  
        return total      
       
    @property
    def get_fightingsfx_total(self):  #get the total no of products related to EnergySfx
        orderfightingsfx = self.orderfightingsfx_set.all()
        total = sum([item.get_total for item in orderfightingsfx]) #sum up the no of quantity of each products related to EnergySfx  
        return total    
    
    @property
    def get_fightingsfx_items(self):  #get the total no of products related to EnergySfx
        orderfightingsfx = self.orderfightingsfx_set.all()
        total = sum([item.quantity for item in orderfightingsfx]) #sum up the no of quantity of each products related to EnergySfx  
        return total    
                
                
 #GRAPHICS TOTAL
    @property  #meaning add property  see cart.html
    def get_landscapes_total(self):  #get total price of all products related to EnergySfx with their respective quantity.
        orderlandscape = self.orderlandscape_set.all()
        total = sum([item.get_total for item in orderlandscape])
        return total    
    
    @property  #meaning add property  see cart.html
    def get_landscapes_items(self):  #get total price of all products related to EnergySfx with their respective quantity.
        orderlandscape = self.orderlandscape_set.all()
        total = sum([item.quantity for item in orderlandscape])
        return total    
    
    @property 
    def get_characters_total(self): 
        ordercharacter = self.ordercharacter_set.all()
        total = sum([item.get_total for item in ordercharacter])
        return total    
    
    @property  #meaning add property  see cart.html
    def get_characters_items(self):  #get total price of all products related to EnergySfx with their respective quantity.
        ordercharacter = self.ordercharacter_set.all()
        total = sum([item.quantity for item in ordercharacter])
        return total     
    
    @property 
    def get_opticallens_total(self): 
        orderopticallenses = self.orderopticallense_set.all()
        total = sum([item.get_total for item in orderopticallenses])
        return total        
    
    @property 
    def get_opticallens_items(self): 
        orderopticallenses = self.orderopticallense_set.all()
        total = sum([item.quantity for item in orderopticallenses])
        return total                  
    
#SpecialcPacks
    @property  
    def get_audiopack_total(self):  
        orderaudiopack= self.ordersoundpack_set.all()
        total = sum([item.get_total for item in orderaudiopack])
        return total    
    
    @property 
    def get_audiopack_items(self):  
        orderaudiopack= self.ordersoundpack_set.all()
        total = sum([item.quantity for item in orderaudiopack])
        return total        
    
    @property  
    def get_vfxpack_total(self):  
        ordervfxpack= self.ordervfxpack_set.all()
        total = sum([item.get_total for item in ordervfxpack])
        return total    
    
    @property  
    def get_vfxpack_items(self):  
        ordervfxpack= self.ordervfxpack_set.all()
        total = sum([item.quantity for item in ordervfxpack])
        return total     
    
    @property  
    def get_flimtransitionpack_total(self):  
        orderflimtransitionpack= self.orderflimtransition_set.all()
        total = sum([item.get_total for item in orderflimtransitionpack])
        return total   
    
    @property  
    def get_flimtransitionpack_items(self):  
        orderflimtransitionpack= self.orderflimtransition_set.all()
        total = sum([item.quantity for item in orderflimtransitionpack])
        return total  
    
    @property  
    def get_motiongraphicspack_total(self):  
        ordermotiongraphicspack= self.ordermotiongraphicspack_set.all()
        total = sum([item.get_total for item in ordermotiongraphicspack])
        return total                          
   
    @property  
    def get_motiongraphicspack_items(self):  
        ordermotiongraphicspack= self.ordermotiongraphicspack_set.all()
        total = sum([item.quantity for item in ordermotiongraphicspack])
        return total        
    
#OTHER
    @property  
    def get_audiospectrum_total(self):  
        orderaudiospectrum = self.orderaudiospectrum_set.all()
        total = sum([item.get_total for item in orderaudiospectrum])
        return total    
    
    @property 
    def get_audiospectrum_items(self): 
        orderaudiospectrum = self.orderaudiospectrum_set.all()
        total = sum([item.quantity for item in orderaudiospectrum])
        return total   
    
    @property  
    def get_lyricstemplate_total(self):  
        orderlyricstemplates = self.orderlyricstemplates_set.all()
        total = sum([item.get_total for item in orderlyricstemplates])
        return total             

    @property  
    def get_lyricstemplate_items(self):  
        orderlyricstemplates = self.orderlyricstemplates_set.all()
        total = sum([item.quantity for item in orderlyricstemplates])
        return total   
     
class PurchasedProducts(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)  #default is false which means unchecked box
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return "Added by "+ str(self.customer)
    
