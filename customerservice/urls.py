from django.urls import path, re_path
# from django.conf.urls import url
from . import views

app_name = 'customerservice'
urlpatterns = [
    # path('index', views.index, name='index'),
    path('', views.Index.as_view(), name='index'),
    path('customers/', views.CustomerListView.as_view(), name='customers'),
    # re_path(r'^customer/(?P<pk>\d+)$', views.CustomerDetailView.as_view(), name='customer-detail'),
    path('customer/<int:pk>', views.CustomerDetailView.as_view(), name='customer-detail'),
    

]