from django.conf.urls import url
from . import views
app_name = 'Supplier'

urlpatterns = [
    url('', views.showSupplier, name = "showSupplier")
]
