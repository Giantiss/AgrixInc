from  django.urls import path
from . import views
app_name = 'vendors'

urlpatterns = [
    path('', views.vendors, name='vendors'),
    path('<vid>/', views.vendor_detail, name='vendor-detail'),
    path('vendors/search/', views.search, name='search'),
]