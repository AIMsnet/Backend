from django.conf.urls import url
from . import views
app_name = 'Supplier'

urlpatterns = [
    url("getUpdateCategory", views.getCategoryUpdate, name = "getUpdateCategory"),
    url("product", views.addProduct, name = "product"),
    url('getCategory', views.getCategory, name="getCategory"),
    url('businessDetail', views.businessUpdate, name = "businessUpdate"),
    url('personalDetail', views.personalUpdate, name = "personalDetails"),
    url('', views.returnPage, name = "returnPage"),
]