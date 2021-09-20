from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin
# Register your models here.

#an way of extending model showing fields in admin section

@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'slug', 'author')
    prepopulated_fields = {'slug': ('title',), }
'''
list display -> list all the attributes side by side
'''

admin.site.register(models.Category)

'''
@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'email',  'publish', 'status')
    list_filter = ('status', 'publish')
    search_fields = ('name', 'email', 'content')
'''

admin.site.register(models.Comment, MPTTModelAdmin)

admin.site.register(models.IpModel)