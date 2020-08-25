from django.conf.urls import url
from . import views

urlpatterns = [
   url('productDescription/(?P<pk>\d+)', views.productDescription, name = "prodcutDescription"),
   url('getProduct', views.getProduct, name = "getProduct"),
   url('(?P<productName>[\w\s,&]+)', views.product, name = "productDisplay"),
]