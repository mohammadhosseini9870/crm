from email.headerregistry import Address
from pyexpat import model
from django.db import models
from django.urls import reverse

class Customer(models.Model):
    commercialname = models.CharField(max_length=50, blank=False, null=False)
    brand = models.CharField(max_length=25, blank=False, null=False)
    address = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return '%s (%s)' % (self.commercialname,self.brand)
        # return self.commercialname
        
    def commercialname_brand(self): #To display in list_display at Adminmodel
        return '%s (%s)' % (self.commercialname,self.brand)
    commercialname_brand.short_description = 'Commercial Name (Brand)'
    
    # def get_absolute_url(self):
    #     return reverse("customerservice/customer-detail", args=[str(self.id)])
        
    def get_absolute_url(self):
        return reverse('customerservice:customer-detail', args=[str(self.id)])
        # return reverse('customer-detail', args=[str(self.id)])
        
    # def display_agent_number(self):
    #     return ', '.join([genre.name for genre in self.genre.all()[:3]])
    #  display_agent_number.short_description = 'Genre'   
        
class Agent(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    mobile = models.CharField(max_length=11)
    rolechoices = (
        ('tec', 'فنی'),
        ('com', 'بازرگانی'),
        ('leg', 'حقوقی'),
    )
    role = models.CharField(max_length=3, choices= rolechoices, default='tec')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # class Meta:
    #     ordering 
    
    def related_customer(self):         #To display in list_display at Adminmodel
        return '%s (%s)' % (self.customer.commercialname,self.customer.brand)
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('customer-detail', args=[str(self.id)])