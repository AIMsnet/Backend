from django.conf.urls import url
from . import views

app_name = 'subCategories'

urlpatterns = [
    url('sub/(?P<subcategory>[\w\s,&]+)/$', views.subCategory, name = "subCategory")
]

