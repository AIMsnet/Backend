from django.conf.urls import url
from . import views

app_name = 'homepage'

urlpatterns = [
    url(r'HomePage', views.home, name = "landingPage"),
    url('SupplierSignIn', views.supplierSignIn, name = "supplierSignIn"),
    url('SupplierSignUp', views.supplierSignUp, name = "supplierSignUp"),
    url('CustomerSignUp', views.customerSignUp, name = "customerSignUp"),
    url('CustomerSignIn', views.customerSignIn, name = "customerSignIn"), 
    url('GovermentQuickLinks', views.GovermentQuick, name = "GovermentQuick")
]