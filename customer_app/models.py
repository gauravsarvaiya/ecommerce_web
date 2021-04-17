from django.db import models
from django.core.validators import RegexValidator
from shop_app.models import shop_items
from django.conf import settings

# Create your models here.

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    Product = models.ForeignKey(shop_items, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quntity = models.IntegerField(default=1)
    

    def __str__(self):
        return self.Product.product_name

    def get_total_item_price(self):
        return self.quntity * self.Product.product_price
    
    
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name
    
    def gst_total(self):
        total = 0
        for i in self.item.all():
            total += i.get_total_item_price()
      
        gst = (total*18)/100
        cgst = (total*18)/100
        net_price = total+gst
        if net_price < 0:
            net_price = 0
        else:
            net_price = net_price
        return round(net_price)

    def get_total(self):
        total = 0
        for i in self.item.all():
            total += i.get_total_item_price()
        return total
    
  