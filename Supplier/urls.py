from django.conf.urls import url
from . import views
app_name = 'Supplier'

urlpatterns = [
    url('(?P<supplierId>[\w\s,&]+)/$', views.getSupplierProfile, name = "getSupplierProfile"),

    url('logout', views.logout, name = "logout"),
    url("productUpdate", views.updateProduct, name = "product"),
    url("getUpdateCategory", views.getCategoryUpdate, name = "getUpdateCategory"),
    url("product", views.addProduct, name = "product"),
    url('getCategory', views.getCategory, name="getCategory"),
    url('businessDetail', views.businessUpdate, name = "businessUpdate"),
    url('personalDetail', views.personalUpdate, name = "personalDetails"),
    url('', views.returnPage, name = "returnPage"),
]

# /(?P<supplierId>[\w\s,&]+)/$