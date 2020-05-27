from django.conf.urls import url
from . import views

urlpatterns = [
   url('', views.product, name = "Product Display"),
]