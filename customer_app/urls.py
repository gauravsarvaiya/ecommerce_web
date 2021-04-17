from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'customer_app'

urlpatterns = [
  path('',views.demo,name='demo'),
  path('add_to_cart/<int:id>',views.add_to_cart,name='add_to_cart'),
  path('cart_details/',views.cart_details.as_view(),name ='cart_details'),
  path('product_list_show/',views.product_list_show.as_view(),name='product_list_show'),
  path('order_summery', views.OrderSummeryView.as_view(), name='order_summery'),
  path('remove_single_item_cart/<int:id>', views.remove_single_item_from_cart, name='remove_single_item_cart')
  
]