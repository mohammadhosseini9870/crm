from django.urls import path, re_path
# from django.conf.urls import url
from . import views

app_name = 'customerservice'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('customers/', views.CustomerListView.as_view(), name='customers'),
    # re_path(r'^customer/(?P<pk>\d+)$', views.CustomerDetailView.as_view(), name='customer-detail'),
    # path('customer/<int:pk>', views.CustomerDetailView.as_view(), name='customer-detail'),
    path('customer/<int:pk>', views.customer_details_with_agent, name='customer-detail-with-agent'),
    path('customer/create', views.CustomerCreate.as_view(), name='customer_create'),
    path('agent/create', views.AgentCreate.as_view(), name='agent_create'),
    # path('customer/create', views.CustomerCreateView.as_view(), name='customer_form'),
    path('customer/<int:pk>/agents/edit/', views.CustmerAgentsEditView.as_view(), name='customer_agent_edit'),

    

]