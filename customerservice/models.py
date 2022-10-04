from cProfile import label
from email.headerregistry import Address
from pyexpat import model
from django.db import models
from django.urls import reverse
# from django.forms import ModelForm

class Customer(models.Model):
    commercialname = models.CharField(max_length=50, blank=False, null=False)
    brand = models.CharField(max_length=25, blank=False, null=False)
    # city = models.CharField(max_length=15, blank=False, null= False)
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
        # return reverse('customerservice:customer-detail', args=[str(self.id)])
        return reverse('customerservice:customer-detail-with-agent', args=[str(self.id)])
        
    # def display_agent_number(self):
    #     return ', '.join([genre.name for genre in self.genre.all()[:3]])
    #  display_agent_number.short_description = 'Genre'   
        
class Agent(models.Model):
    name = models.CharField(max_length=25, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    phone = models.CharField(max_length=11, verbose_name='تلفن')
    mobile = models.CharField(max_length=11, verbose_name='تلفن همراه')
    rolechoices = (
        ('tec', 'فنی'),
        ('com', 'بازرگانی'),
        ('leg', 'حقوقی'),
    )
    role = models.CharField(max_length=3, choices= rolechoices, default='tec', verbose_name='نقش نماینده')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='نام مشترک')
    # class Meta:
    #     ordering 
    
    def related_customer(self):         #To display in list_display at Adminmodel
        return '%s (%s)' % (self.customer.commercialname,self.customer.brand)
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('customerservice:customer-detail-with-agent', args=[str(self.id)])
    
class Wireless(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=False, null=False)
    popsite_choices = (
        ('بوتان', 'بوتان'),
        ('شریعتی', 'شریعتی'),
        ('زرین', 'زرین'),
        ('کردستان', 'کردستان'),
        ('سنایی', 'سنایی'),
        ('پلاستیران', 'پلاستیران'),
    )
    popsite = models.CharField(max_length=25, choices=popsite_choices, blank=False, null=False)
    # t stands for transmit, r for recieve
    internet_t_bw = models.BigIntegerField(blank=True, null=True)
    internet_r_bw = models.BigIntegerField(blank=True, null=True)
    interanet_t_bw = models.BigIntegerField(blank=True, null=True)
    interanet_r_bw = models.BigIntegerField(blank=True, null=True)
    throughput_t_bw = models.BigIntegerField(blank=True, null=True)
    throughput_r_bw = models.BigIntegerField(blank=True, null=True)
    notes = models.CharField(max_length=500)
    
class Cloud(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=False, null=False)
    sizechoices = (
        ('micro', 'Micro'),
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
        ('xlarge', 'XLarge'),
        ('xxlarge', 'XXLarge'),
    )
    size = models.CharField(max_length=7, choices=sizechoices, default='medium', blank=False, null=False)
    

# class CustomerForm(ModelForm):
#     class Meta:
#         model = Customer
#         fields = '__all__'
#         # fields = ['commercialname', 'brand']    