from django.db import models
from EHub.models import *
from decimal  import Decimal
#Create your models here.

class AudioSpectrum(models.Model):
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
    paidproduct = models.FileField(upload_to="OTHERS/AudioSpectrum/paid/%y"
                                    ,help_text="Provide a DemoVideo. This product is just a showcase to Customers. Only .mp4 and .mov are accepted"
                                    ,validators=[FileExtensionValidator(['mp4','mov']),]
                                    ,null=True)
    freeproduct = models.FileField(upload_to="OTHERS/AudioSpectrum/free/%y"
                                    ,help_text="Provide a file to distribute to Customers .Only .zip and .rar are accepted"
                                    ,validators=[FileExtensionValidator(['zip','rar'])]
                                     ,null=True)
    date_published=models.DateField(auto_now_add=True,null=True)
    
    def __str__(self):
        return str(self.name)

class OrderAudioSpectrum(models.Model):  #make more orderitem
    TYPE_CHOICES = (
        ('FREE', 'FREE'),
        ('PAID', 'PAID'),                           
    )
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)    
    product = models.ForeignKey(AudioSpectrum, on_delete=models.SET_NULL, blank=True, null=True)  #it's gonna give you what you actually define in  def__str___.....return self.name
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    addtoDpage = models.ForeignKey(PurchasedProducts, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    complete = models.BooleanField(default=False, null=True, blank=False)  #default is false which means unchecked box
    data_added = models.DateTimeField(auto_now_add=True)
    published_by=models.CharField(null=True,max_length=20)

    def __str__(self):
        return str(self.product)

    @property 
    def get_total(self):    
        total = self.product.price * self.quantity 
        return total          
    
class LyricsTemplate(models.Model):
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
    paidproduct = models.FileField(upload_to="OTHERS/Lightining/paid/%y"
                                    ,help_text="Provide a DemoVideo.This product is just a showcase to Customers. Only .mp4 and .mov are accepted."
                                    ,validators=[FileExtensionValidator(['mp4','mov']),]
                                     ,null=True)
    freeproduct = models.FileField(upload_to="OTHERS/Lightining/free/%y"
                                    ,help_text="Provide a file to distribute to Customers .Only .zip and .rar are accepted"
                                    ,validators=[FileExtensionValidator(['zip','rar'])]
                                    ,null=True)
    date_published=models.DateField(auto_now_add=True,null=True)
    
    def __str__(self):
        return str(self.name)    
    
class OrderLyricsTemplates(models.Model):  #make more orderitem
    TYPE_CHOICES = (
        ('FREE', 'FREE'),
        ('PAID', 'PAID'),                           
    )
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)    
    product = models.ForeignKey(LyricsTemplate, on_delete=models.SET_NULL, blank=True, null=True)  #it's gonna give you what you actually define in  def__str___.....return self.name
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
   
    