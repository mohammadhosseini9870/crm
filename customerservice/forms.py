from dataclasses import fields
import imp
from pyexpat import model
from socket import fromshare
from tkinter import Widget
# from django import froms
from .models import Customer, Agent
# from . import models
from django.forms import ModelForm
from django.forms.models import inlineformset_factory, InlineForeignKeyField
from django.core.exceptions import ValidationError
# from django.utils.translation import ugettext_lazy as _


CustomerAgentsFormset = inlineformset_factory(Customer, Agent, fields=('name', 'email', 'phone', 'mobile', 'role', 'customer'),extra= 2, can_delete=True)

# class CustomerForm(ModelForm):
#     class Meta:
#         model = Customer
#         # fields = '__all__'
#         fields = ['commercialname', 'brand', ]
#         # Widget = 

# class AgentForm(ModelForm):
#     class Meta:
#         model = Agent
#         fields = '__all__'

# AgentInlineFormset = inlineformset_factory(Customer, Agent,form=AgentForm, extra=1, can_delete=True)
