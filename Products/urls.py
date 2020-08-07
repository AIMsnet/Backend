from django.conf.urls import url
from . import views

urlpatterns = [
   url('productDescription', views.productDescription, name = "prodcutDescription"),
   url('', views.product, name = "productDisplay"),
]