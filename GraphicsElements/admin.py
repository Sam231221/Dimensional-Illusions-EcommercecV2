from django.contrib import admin
from GraphicsElements.models import *
# Register your models here.
admin.site.register(Characters)
admin.site.register(OpticalLens)
admin.site.register(Landscapes)
admin.site.register(OrderOpticalLense)
admin.site.register(OrderLandscape)
admin.site.register(OrderCharacter)