from django.db import models
from django.contrib.auth.models import User
from decimal  import Decimal
from EHub.models import *

# Create your models here.

class LightiningSfx(models.Model):
    TYPE_CHOICES = (
        ('FREE', 'FREE'),
        ('PAID', 'PAID'),                           
    )      
    publisher= models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    type=models.CharField(max_length=20, choices=TYPE_CHOICES,null=True)       
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=6,max_length=4
                                ,help_text="Set the price to 0 if the product type is free."
                                ,validators=[MinValueValidator(Decimal('0'))]
                                ,decimal_places=2)
    paidproduct = models.FileField(upload_to="SFX/Lightining/paid/%y"
                                    ,help_text="Provide a WatermarkProduct.This product is just a showcase to Customers. Only .mp3 is  accepted"
                                    ,validators=[FileExtensionValidator(['mp3'])]
                                    ,null=True,blank=True)
    freeproduct = models.FileField(upload_to="SFX/Lightining/free/%y"
                                    ,help_text="Provide a Watermark free Product to distribute to Customers. Only .mp3 is  accepted"
                                    ,validators=[FileExtensionValidator(['mp3'])]
                                    ,null=True,blank=True)
    date_published=models.DateField(auto_now_add=True,null=True)
      
    def __str__(self):
        return str(self.name)

class OrderLightiningSfx(models.Model):  #make more orderitem
    TYPE_CHOICES = (
        ('FREE', 'FREE'),
        ('PAID', 'PAID'),                           
    )
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)    
    product = models.ForeignKey(LightiningSfx, on_delete=models.SET_NULL, blank=True, null=True)  #it's gonna give you what you actually define in  def__str___.....return self.name
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    addtoDpage = models.ForeignKey(PurchasedProducts, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    complete = models.BooleanField(default=False, null=True, blank=False)  #default is false which means unchecked box
    data_added = models.DateTimeField(auto_now_add=True)
    published_by=models.CharField(null=True,max_length=20)

    def __str__(self):
        return str(self.product)

    @property 
    def get_total(self):    #to get total items of a certain product in cart.html
        total = self.product.price * self.quantity  #+self.product1.price * self.quantity
        return total                 
    
class EnvironmentalSfx(models.Model):
    TYPE_CHOICES = (
        ('FREE', 'FREE'),
        ('PAID', 'PAID'),                           
    )
    publisher= models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)  
    type=models.CharField(max_length=20, choices=TYPE_CHOICES,null=True)       
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=6,max_length=4
                                ,help_text="Set the price to 0 if the product type is free."
                                ,validators=[MinValueValidator(Decimal('0'))]
                                ,decimal_places=2)
    paidproduct = models.FileField(upload_to="SFX/Environment/free/%y"
                                    ,help_text="Provide a WatermarkProduct.This product is just a showcase to Customers. Only .mp3 is  accepted"
                                    ,validators=[FileExtensionValidator(['mp3']),]
                                    ,null=True,blank=True)
    freeproduct = models.FileField(upload_to="SFX/Environment/paid/%y"
                                    ,help_text="Provide a Watermark free Product to distribute to Customers. Only .mp3 is  accepted"
                                    ,validators=[FileExtensionValidator(['mp3']),]
                                    ,null=True,blank=True)
    date_published=models.DateField(auto_now_add=True,null=True)
    
    def __str__(self):
        return str(self.name)
    
class OrderEnvironmentalSfx(models.Model):  #make more orderitem
    TYPE_CHOICES = (
        ('FREE', 'FREE'),
        ('PAID', 'PAID'),                           
    )
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)    
    product = models.ForeignKey(EnvironmentalSfx, on_delete=models.SET_NULL, blank=True, null=True)  #it's gonna give you what you actually define in  def__str___.....return self.name
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    addtoDpage = models.ForeignKey(PurchasedProducts, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    complete = models.BooleanField(default=False, null=True, blank=False)  #default is false which means unchecked box
    data_added = models.DateTimeField(auto_now_add=True)
    published_by=models.CharField(null=True,max_length=20)

    def __str__(self):
        return str(self.product)

    @property 
    def get_total(self):    #to get total items of a certain product in cart.html
        total = self.product.price * self.quantity  #+self.product1.price * self.quantity
        return total          

class  FireSfx(models.Model):
    TYPE_CHOICES = (
        ('FREE', 'FREE'),
        ('PAID', 'PAID'),                           
    ) 
    publisher= models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    type=models.CharField(max_length=20, choices=TYPE_CHOICES,null=True)       
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=6,max_length=4
                                ,help_text="Set the price to 0 if the product type is free."
                                ,validators=[MinValueValidator(Decimal('0'))]
                                ,decimal_places=2)
    paidproduct = models.FileField(upload_to="SFX/Fire/free/%y"
                                    ,help_text="Provide a WatermarkProduct.This product is just a showcase to Customers. Only .mp3 is  accepted"
                                    ,validators=[FileExtensionValidator(['mp3']),]
                                    ,null=True,blank=True)
    freeproduct = models.FileField(upload_to="SFX/Fire/paid/%y"
                                    ,help_text="Provide a Watermark free Product to distribute to Customers. Only .mp3 is  accepted"
                                    ,validators=[FileExtensionValidator(['mp3']),]
                                    ,null=True,blank=True)
    date_published=models.DateField(auto_now_add=True,null=True)
        
    def __str__(self):
        return str(self.name)     
        
class OrderFireSfx(models.Model):  #make more orderitem
    TYPE_CHOICES = (
        ('FREE', 'FREE'),
        ('PAID', 'PAID'),                           
    )
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)    
    product = models.ForeignKey(FireSfx, on_delete=models.SET_NULL, blank=True, null=True)  #it's gonna give you what you actually define in  def__str___.....return self.name
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    addtoDpage = models.ForeignKey(PurchasedProducts, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    complete = models.BooleanField(default=False, null=True, blank=False)  #default is false which means unchecked box
    data_added = models.DateTimeField(auto_now_add=True)
    published_by=models.CharField(null=True,max_length=20)

    def __str__(self):
        return str(self.product)

    @property 
    def get_total(self):    #to get total items of a certain product in cart.html
        total = self.product.price * self.quantity  #+self.product1.price * self.quantity
        return total      
            
class   MachinerySfx(models.Model):
    TYPE_CHOICES = (
        ('FREE', 'FREE'),
        ('PAID', 'PAID'),                           
    )
    publisher= models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)  
    type=models.CharField(max_length=20, choices=TYPE_CHOICES,null=True)       
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=6,max_length=4
                                ,help_text="Set the price to 0 if the product type is free."
                                ,validators=[MinValueValidator(Decimal('0'))]
                                ,decimal_places=2)
    paidproduct = models.FileField(upload_to="SFX/Machinery/free/%y"
                                    ,help_text="Provide a WatermarkProduct.This product is just a showcase to Customers. Only .mp3 is  accepted"
                                    ,validators=[FileExtensionValidator(['mp3']),]
                                    ,null=True,blank=True)
    freeproduct = models.FileField(upload_to="SFX/Machinery/paid/%y"
                                    ,help_text="Provide a Watermark free Product to distribute to Customers. Only .mp3 is  accepted"
                                    ,validators=[FileExtensionValidator(['mp3']),]
                                    ,null=True,blank=True)
    date_published=models.DateField(auto_now_add=True,null=True)
    
    def __str__(self):
        return str(self.name)        
 
class OrderMachinerySfx(models.Model):  #make more orderitem
    TYPE_CHOICES = (
        ('FREE', 'FREE'),
        ('PAID', 'PAID'),                           
    )
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)    
    product = models.ForeignKey(MachinerySfx, on_delete=models.SET_NULL, blank=True, null=True)  #it's gonna give you what you actually define in  def__str___.....return self.name
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    addtoDpage = models.ForeignKey(PurchasedProducts, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    complete = models.BooleanField(default=False, null=True, blank=False)  #default is false which means unchecked box
    data_added = models.DateTimeField(auto_now_add=True)
    published_by=models.CharField(null=True,max_length=20)

    def __str__(self):
        return str(self.product)

    @property 
    def get_total(self):    #to get total items of a certain product in cart.html
        total = self.product.price * self.quantity  #+self.product1.price * self.quantity
        return total             
               
class EnergySfx(models.Model):
    TYPE_CHOICES = (
        ('FREE', 'FREE'),
        ('PAID', 'PAID'),                           
    )   
    publisher= models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    type=models.CharField(max_length=20, choices=TYPE_CHOICES,null=True)       
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=6,max_length=4
                                ,help_text="Set the price to 0 if the product type is free."
                                ,validators=[MinValueValidator(Decimal('0'))]
                                ,decimal_places=2)
    paidproduct = models.FileField(upload_to="SFX/Energy/free/%y"
                                    ,help_text="Provide a WatermarkProduct.This product is just a showcase to Customers. Only .mp3 is  accepted"
                                    ,validators=[FileExtensionValidator(['mp3']),]
                                    ,null=True,blank=True)
    freeproduct = models.FileField(upload_to="SFX/Energy/paid/%y"
                                    ,help_text="Provide a Watermark free Product to distribute to Customers .Only .mp3 is accepted"
                                    ,validators=[FileExtensionValidator(['mp3']),]
                                    ,null=True,blank=True)
    date_published=models.DateField(auto_now_add=True,null=True)
    
    def __str__(self):
        return str(self.name)   

class OrderEnergySfx(models.Model):  #make more orderitem
    TYPE_CHOICES = (
        ('FREE', 'FREE'),
        ('PAID', 'PAID'),                           
    )
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)    
    product = models.ForeignKey(EnergySfx, on_delete=models.SET_NULL, blank=True, null=True)  #it's gonna give you what you actually define in  def__str___.....return self.name
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    addtoDpage = models.ForeignKey(PurchasedProducts, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    complete = models.BooleanField(default=False, null=True, blank=False)  #default is false which means unchecked box
    data_added = models.DateTimeField(auto_now_add=True)
    published_by=models.CharField(null=True,max_length=20)

    def __str__(self):
        return str(self.product)

    @property 
    def get_total(self):    #to get total items of a certain product in cart.html
        total = self.product.price * self.quantity  #+self.product1.price * self.quantity
        return total          
         
class WeaponsSfx(models.Model):
    TYPE_CHOICES = (
        ('FREE', 'FREE'),
        ('PAID', 'PAID'),                           
    )
    publisher= models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)  
    type=models.CharField(max_length=20, choices=TYPE_CHOICES,null=True)       
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=6,max_length=4
                                ,help_text="Set the price to 0 if the product type is free."
                                ,validators=[MinValueValidator(Decimal('0'))]
                                ,decimal_places=2)
    paidproduct = models.FileField(upload_to="SFX/Weapons/free/%y"
                                    ,help_text="Provide a WatermarkProduct.This product is just a showcase to Customers.Only .mp3 is  accepted"
                                    ,validators=[FileExtensionValidator(['mp3']),]
                                    ,null=True,blank=True)
    freeproduct = models.FileField(upload_to="SFX/Weapons/paid/%y"
                                    ,help_text="Provide a Watermark free Product to distribute to Customers .Only .mp3 is  accepted"
                                    ,validators=[FileExtensionValidator(['mp3']),]
                                    ,null=True,blank=True)
    date_published=models.DateField(auto_now_add=True,null=True)  
  
    def __str__(self):
        return str(self.name)
    
class OrderWeaponsSfx(models.Model):  #make more orderitem
    TYPE_CHOICES = (
        ('FREE', 'FREE'),
        ('PAID', 'PAID'),                           
    )
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)    
    product = models.ForeignKey(WeaponsSfx, on_delete=models.SET_NULL, blank=True, null=True)  #it's gonna give you what you actually define in  def__str___.....return self.name
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    addtoDpage = models.ForeignKey(PurchasedProducts, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    complete = models.BooleanField(default=False, null=True, blank=False)  #default is false which means unchecked box
    data_added = models.DateTimeField(auto_now_add=True)
    published_by=models.CharField(null=True,max_length=20)

    def __str__(self):
        return str(self.product)

    @property 
    def get_total(self):    #to get total items of a certain product in cart.html
        total = self.product.price * self.quantity  #+self.product1.price * self.quantity
        return total      
         
class FightingSfx(models.Model):
    TYPE_CHOICES = (
        ('FREE', 'FREE'),
        ('PAID', 'PAID'),                           
    )
    publisher= models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)    
    type=models.CharField(max_length=20, choices=TYPE_CHOICES,null=True)       
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=6,max_length=4
                                ,help_text="Set the price to 0 if the product type is free."
                                ,validators=[MinValueValidator(Decimal('0'))]
                                ,decimal_places=2)
    paidproduct = models.FileField(upload_to="SFX/Fighting/free/%y"
                                    ,help_text="Provide a WatermarkProduct.This product is just a showcase to Customers. Only .mp3 is  accepted"
                                    ,validators=[FileExtensionValidator(['mp3']),]
                                    ,null=True,blank=True)
    freeproduct = models.FileField(upload_to="SFX/Fighting/paid/%y"
                                    ,help_text="Provide a Watermark free Product to distribute to Customers .Only .mp3 is  accepted"
                                    ,validators=[FileExtensionValidator(['mp3']),]
                                    ,null=True,blank=True)
    date_published=models.DateField(auto_now_add=True,null=True)
      
    def __str__(self):
        return str(self.name)        
 
class OrderFightingSfx(models.Model):  #make more orderitem
    TYPE_CHOICES = (
        ('FREE', 'FREE'),
        ('PAID', 'PAID'),                           
    )
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)    
    product = models.ForeignKey(FightingSfx, on_delete=models.SET_NULL, blank=True, null=True)  #it's gonna give you what you actually define in  def__str___.....return self.name
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    addtoDpage = models.ForeignKey(PurchasedProducts, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    complete = models.BooleanField(default=False, null=True, blank=False)  #default is false which means unchecked box
    data_added = models.DateTimeField(auto_now_add=True)
    published_by=models.CharField(null=True,max_length=20)

    def __str__(self):
        return str(self.product)

    @property 
    def get_total(self):    #to get total items of a certain product in cart.html
        total = self.product.price * self.quantity  #+self.product1.price * self.quantity
        return total      
          
  