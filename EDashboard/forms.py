from django import forms
from VFX.models import *
from SFX.models import *
from OTHERS.models import *
from GraphicsElements.models import *
from SpecialPacks.models import *
from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy
from .models import *
# Create your models here.

class ProfileForm(ModelForm):
    error_messages = {
		'required': ugettext_lazy("This field is mandatory."),
		'invalid': 'Enter a valid number',
		'caps': 'This field if case sensitive' 
		}

    esewa_id = forms.CharField(error_messages=error_messages,
     label='Esewa_Id',
     help_text='This information will be used only for payment purpose.',
     widget=forms.NumberInput(attrs={'class':'NumberField', 'type':'number', 'placeholder':'Enter your Esewa_Id'}),

     )
    class Meta:
	    model=Customer
	    fields = ['first_name','second_name','email','image','gender','esewa_id']
    
        
class EnergyVfxForm(ModelForm):
			def __init__(self, *args, **kwargs):
				super().__init__(*args, **kwargs)

				self.fields['publisher'].widget.attrs.update(  #remove the select option
					{'class': 'd-none'})
				self.fields['publisher'].label = ''#remove the label element for parent(text wont appear)
				self.fields['publisher'].required = False #to remove input required atttribute for parent so its gonna be optional
				self.fields['publisher'].select =''              
               
			class Meta:
				model=EnergyVfx
				fields = '__all__'

				
class LandscapeForm(ModelForm):
#this function 
			def __init__(self, *args, **kwargs):
				super().__init__(*args, **kwargs)

				self.fields['publisher'].widget.attrs.update(  #remove the select option
					{'class': 'd-none'})
				self.fields['publisher'].label = ''#remove the label element for parent(text wont appear)
				self.fields['publisher'].required = False #to remove input required atttribute for parent so its gonna be optional
			
			class Meta:
				model=Landscapes
				fields = '__all__'  
    

class CharacterForm(ModelForm):
    
			def __init__(self, *args, **kwargs):
				super().__init__(*args, **kwargs)

				self.fields['publisher'].widget.attrs.update(  #remove the select option
					{'class': 'd-none'})
				self.fields['publisher'].label = ''#remove the label element for parent(text wont appear)
				self.fields['publisher'].required = False #to remove input required atttribute for parent so its gonna be optional
				self.fields['publisher'].select =''              
                   
			class Meta:
				model=Characters
				fields = '__all__'  				
    