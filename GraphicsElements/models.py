from django.db import models
from EHub.models import *


from decimal  import Decimal
from django.core.validators import FileExtensionValidator,MinValueValidator
# Create your models here.

class  Landscapes(models.Model):
    TYPE_CHOICES = (
        ('FREE', 'FREE'),
        ('PAID', 'PAID'),                           
    )   
    CATEGORY_CHOICES = (
        ('2D','2D'),
        ('3D','3D'),
    )  
    
    class FreeLandscapeManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(TYPE_CHOICES='FREE')
        
    class PaidLandscapeManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(TYPE_CHOICES='PAID')        

    publisher= models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)     
    type=models.CharField(max_length=20, choices=TYPE_CHOICES
                          ,help_text="Choose the Product type. Is it for free? or paid?"
                          ,null=True)       
    name = models.CharField(max_length=200,unique=True, null=True)
    category=models.CharField(max_length=20, choices=CATEGORY_CHOICES,blank=True,null=True)    
       
    price = models.DecimalField(max_digits=6
                                ,help_text="Set the price to 0 if the product type is free."
                                ,validators=[MinValueValidator(Decimal('0'))]
                                ,decimal_places=2)

    paidproduct = models.ImageField(upload_to="GraphicsElements/paid/Landscapes/%y"
                                    ,help_text="Provide a WatermarkProduct.This product is just a showcase to Customers. Only .png and .jpg are accepted"
                                    ,validators=[FileExtensionValidator(['png','jpg']),]
                                    ,null=True,blank=True)
    freeproduct = models.ImageField(upload_to="GraphicsElements/free/Landscapes/%y"
                                    ,help_text="Provide a Watermark free Product to distribute to Customers .Only .png and .jpg are accepted"
                                    ,validators=[FileExtensionValidator(['png','jpg']),]
                                    ,null=True,blank=True)
    date_published=models.DateField(auto_now_add=True,null=True)
    
    def __str__(self):
        return str(self.name)        
    
class OrderLandscape(models.Model):  #make more orderitem
    TYPE_CHOICES = (
        ('FREE', 'FREE'),
        ('PAID', 'PAID'),                           
    )    
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(Landscapes, on_delete=models.SET_NULL, blank=True, null=True)  #it's gonna give you what you actually define in  def__str___.....return self.name
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
    
class   Characters(models.Model):
    TYPE_CHOICES = (
        ('FREE', 'FREE'),
        ('PAID', 'PAID'),                           
    )  
    CATEGORY_CHOICES = (
        ('2D','2D'),
        ('3D','3D'),
    )  
    class FreeCharacterManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(TYPE_CHOICES='FREE')
        
    class PaidCharacterManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(TYPE_CHOICES='PAID')      
             
    publisher= models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)  
    type=models.CharField(max_length=20, choices=TYPE_CHOICES
                          ,help_text="Choose the Product type. Is it for free? or paid?"
                          ,null=True)       
    name = models.CharField(max_length=200,unique=True, null=True)
    price = models.DecimalField(max_digits=6
                                ,help_text="Set the price to 0 if the product type is free."
                                ,validators=[MinValueValidator(Decimal('0'))]
                                ,decimal_places=2)
    category=models.CharField(max_length=20, choices=CATEGORY_CHOICES,blank=True,null=True)    
    
    paidproduct = models.ImageField(upload_to="GraphicsElements/paid/Characters/%y"
                                    ,help_text="Provide a WatermarkProduct.This product is just a showcase to Customers. Only .png and .jpg are accepted"
                                    ,validators=[FileExtensionValidator(['png','jpg']),]
                                    ,null=True,blank=True)
    freeproduct = models.ImageField(upload_to="GraphicsElements/free/Landscapes/%y"
                                    ,help_text="Provide a Watermark free Product to distribute to Customers .Only .png and .jpg are accepted"
                                    ,validators=[FileExtensionValidator(['png','jpg']),]
                                    ,null=True,blank=True)
    
    date_published=models.DateField(auto_now_add=True,null=True)

    def __str__(self):
        return str(self.name)          
 
class OrderCharacter(models.Model):  #make more orderitem
    TYPE_CHOICES = (
        ('FREE', 'FREE'),
        ('PAID', 'PAID'),                           
    )
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)    
    product = models.ForeignKey(Characters, on_delete=models.SET_NULL, blank=True, null=True)  #it's gonna give you what you actually define in  def__str___.....return self.name
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
    
class  OpticalLens(models.Model):
    TYPE_CHOICES = (
        ('FREE', 'FREE'),
        ('PAID', 'PAID'),                           
    )
    CATEGORY_CHOICES = (
        ('2D','2D'),
        ('3D','3D'),
    )   
    publisher= models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)     
    type=models.CharField(max_length=20, choices=TYPE_CHOICES
                          ,help_text="Choose the Product type. Is it for free? or paid?"
                          ,null=True)       
    name = models.CharField(max_length=200,unique=True, null=True)
    price = models.DecimalField(max_digits=4
                                ,validators=[MinValueValidator(Decimal('0'))]
                                ,help_text="Set the price to 0 if the product type is free."
                                ,decimal_places=2)
    category=models.CharField(max_length=20, choices=CATEGORY_CHOICES,blank=True,null=True)
    paidproduct = models.ImageField(upload_to="GraphicsElements/paid/OpticalLense/%y"
                                    ,help_text="Provide a WatermarkProduct.This product is just a showcase to Customers. Only .png and .jpg are accepted"
                                    ,validators=[FileExtensionValidator(['png','jpg']),]
                                    ,null=True,blank=True)
    freeproduct = models.ImageField(upload_to="GraphicsElements/free/OpticalLense/%y"
                                    ,help_text="Provide a Watermark free Product to distribute to Customers .Only .png and .jpg are accepted"
                                    ,validators=[FileExtensionValidator(['png','jpg']),]
                                    ,null=True,blank=True)
    date_published=models.DateField(auto_now_add=True,null=True)

    def __str__(self):
        return str(self.name)  
    
class OrderOpticalLense(models.Model):  #make more orderitem
    TYPE_CHOICES = (
        ('FREE', 'FREE'),
        ('PAID', 'PAID'),                           
    )  
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)  
    product = models.ForeignKey(OpticalLens, on_delete=models.SET_NULL, blank=True, null=True)  #it's gonna give you what you actually define in  def__str___.....return self.name
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