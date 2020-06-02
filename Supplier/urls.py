from django.conf.urls import url
from . import views
app_name = 'Supplier'

urlpatterns = [
    url('(?P<email>[\w\s,@.]+)', views.showSupplier, name = "showSupplier")
]
