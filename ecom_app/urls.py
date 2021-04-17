from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'ecom_app'

urlpatterns = [
   path('',views.home,name='home'),
   path('shop_register/',views.shop_register,name='shop_register'),
   path('customer_register/',views.customer_register,name='customer_register'),
   path('ecom_login/',views.ecom_login,name='ecom_login'),
   path('ecom_logout/',views.ecom_logout,name='ecom_logout'),
]