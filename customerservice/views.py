from cProfile import label
from email import message
from http.client import HTTPResponse
from multiprocessing import context
from tkinter import Label
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponseRedirect
from . import models
from django.template.loader import render_to_string
from django.db import transaction
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import CreateView, UpdateView, DeleteView, FormView
from extra_views import FormSetView
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.forms import modelformset_factory
from django.views.generic.detail import SingleObjectMixin
# from .forms import CustomerForm, AgentForm, AgentInlineFormset
from .forms import CustomerAgentsFormset

# @login_required
# def index(request):
#     num_customer = models.Customer.objects.all().count()
#     num_agent = models.Agent.objects.all().count()
#     context = {'num_customer' : num_customer, 'num_agent' : num_agent}
#     return render(request, 'index.html', context)

class Index(LoginRequiredMixin, generic.TemplateView):
    login_url = '/accounts/login/'
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_customers'] = models.Customer.objects.all()[:5]
        context = {'num_customer' : models.Customer.objects.all().count(), 'num_agent' : models.Agent.objects.all().count()}
        return context


class CustomerListView(LoginRequiredMixin, generic.ListView):
    #name of class: ClassnameListView / name of list that is sent to template: classname_list
    #name of template_name we must create for it: classname_list.html
    model = models.Customer #template_name = customer_list.html context = customer_list
    # context_object_name = 'my_customer_list'
    # queryset = models.Customer.objects.filter(brand__icontains = 'thing')
    # def  get_queryset(self):
    #     return models.Customer.objects.filter(brand__icontains = 'thing')[:5]
    template_name = 'customer_list.html'
    login_url = '/accounts/login/'
    # redirect_field_name = ''

    
class CustomerDetailView(generic.DetailView):# min 10
    model = models.Customer 
    # model: [models.Customer,models.Agent]
    template_name = 'customer_detail.html'
    # context = {}
    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['book_list'] = Book.objects.all()
    #     return context
    
    
    
    
    # template_name = 'customerservice/customer_detail.html'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs) 
    #     # context['now'] = timezone.now()
    #     context = {'customer' : models.Customer.objects.all().count()}
    #     return context
    # template_name = 'customerservice:customer_detail.html'
    #name of class: ClassnameDetailView
    #name of list that is sent to template: classname
    #name of template_name we must create for it: classname_detail.html
    
    # template_name = 'custoasdasdmer_detail.html'
    
    
    #get-query-set
    #default template-name= Classname_List
    #context_object_name: Optional[str] your own name for the list as a template variable
    
    # def get_queryset(self) -> _SupportsPagination[_M]:  
    #     return super().get_queryset()
    
    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     return super().get_context_data(**kwargs)
    
def customer_details_with_agent(request, pk):
    # template_name = 'customer_details_with_agent'
    customer = models.Customer.objects.get(id=pk)
    # agent = models.Agent.objects.all().count()
    agent = customer.agent_set.all()
    # customer.get_queryset(self)  
    context = {'customer' : customer, 'agent': agent}
    # context = {'customer' : customer}
    return render(request, 'customer_details_with_agent.html', context)

class CustomerCreate(CreateView):
    model = models.Customer
    fields = '__all__'
    template_name = 'customer_form.html'
    # initial = {'':}
    # success_url = reverse_lazy('customerservice:customers')

class AgentCreate(CreateView):
    model = models.Agent
    fields = '__all__'
    template_name = 'agent_form.html'

class CustmerAgentsEditView (SingleObjectMixin, FormView):
    model = models.Agent
    template_name = 'customer_agents_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=models.Customer.objects.all())
        # object.fields[].label='حذف'
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=models.Customer.objects.all())
        return super().post(request, *args, **kwargs)
    
    def get_form(self, form_class=None):
        return CustomerAgentsFormset(**self.get_form_kwargs(), instance=self.object)
    
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse('customerservice:customer-detail-with-agent', kwargs={'pk': self.object.pk})
        # return reverse('customerservice:customer-detail-with-agent', kwargs={'pk': self.object.pk})
        
        
    
# class CustomerCreateView(CreateView):
#     form_class = CustomerForm
#     template_name = 'customer_form.html'
    
#     def get_context_data(self,  **kwargs):
#         context = super(CustomerCreateView, self).get_context_data(**kwargs)
#         context['agent_formset'] = AgentInlineFormset()
#         return context
    
#     def post(self, request, *args, **kwargs):
#         self.object = None
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         agent_formset = AgentInlineFormset(self.request.POST)
#         if form.is_valid() and agent_formset.is_valid():
#             return self.form_valid(form, agent_formset)
#         else:
#             return self.form_invalid(form, agent_formset)
        
#     def form_valid(self, form, agent_formset):
#         self.object = form.save(commit=False)
#         self.object.save()
#         # saving Agent Instances
#         agent = agent_formset.save(commit=False)
#         for meta in agent:
#             meta.customer = self.object
#             meta.save()
#         return redirect(reverse('customerservice:customers'))
#     def form_invalid(self, form, agent_formset):
#         return self.render_to_response(
#             self.get_context_data(form=form,agent_formset=agent_formset))    
        
    