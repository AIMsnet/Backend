from django.conf.urls import url
from . import views
app_name = 'Supplier'

urlpatterns = [
    url('businessDetail', views.businessUpdate, name = "businessUpdate"),
    url('personalDetail', views.personalUpdate, name = "personalDetails"),
    url('', views.returnPage, name = "returnPage"),
    
]