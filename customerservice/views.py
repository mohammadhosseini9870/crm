from multiprocessing import context
from django.shortcuts import render
from . import models
from django.views import generic
# from django.views.generic.detail import DetailView

# def index(request):
#     num_customer = models.Customer.objects.all().count()
#     num_agent = models.Agent.objects.all().count()
#     context = {'num_customer' : num_customer, 'num_agent' : num_agent}
#     return render(request, 'index.html', context)

#---------------------------------------------

class Index(generic.TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['latest_customers'] = models.Customer.objects.all()[:5]
        context = {'num_customer' : models.Customer.objects.all().count(), 'num_agent' : models.Agent.objects.all().count()}
        return context


class CustomerListView(generic.ListView):
    #name of class: ClassnameListView
    #name of list that is sent to template: classname_list
    #name of template_name we must create for it: classname_list.html
    model = models.Customer #template_name = customer_list.html context = customer_list
    # context_object_name = 'my_customer_list'
    # queryset = models.Customer.objects.filter(brand__icontains = 'thing')
    # def  get_queryset(self):
    #     return models.Customer.objects.filter(brand__icontains = 'thing')[:5]
    template_name = 'customer_list.html'
    
class CustomerDetailView(generic.DetailView):# min 10
    # pass
    model = models.Customer 
    template_name = 'customer_detail.html'
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
    
    