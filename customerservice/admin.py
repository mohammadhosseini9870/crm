from pyexpat import model
from django.contrib import admin
from . import models

class AgentInline(admin.TabularInline):
    model = models.Agent
    extra = 1

#-----------------------------

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    # model = Customer
    # list_display = ('commercialname', 'brand', 'address')
    list_display = ('commercialname_brand', 'address')
    list_filter = ('commercialname', 'brand', 'address')
    fields = (('commercialname', 'brand'), 'address')
    inlines = [AgentInline]
# admin.site.register(models.Customer, CustomerAdmin)   
 
#-----------------------------

@admin.register(models.Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'related_customer')
    
# admin.site.register(models.Agent)


