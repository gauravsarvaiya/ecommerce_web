from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'shop_app'

urlpatterns = [
  path('',views.demo,name='demo'),
  path('shop_info/',views.shop_info.as_view(),name='shop_info'),
  path('product_list/',views.product_list.as_view(),name='product_list'),
  path('product_update/<int:pk>',views.product_update.as_view(),name ='product_update'),
  path('product_delete/<int:pk>',views.product_delete.as_view(),name ='product_delete'),
  path('product_details/<int:pk>',views.product_details.as_view(),name ='product_details'),
  
]