from django.db import models
from ecom_app.models import *
from django.conf import settings

class shop_items(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    product_name = models.CharField(max_length = 20)
    product_price = models.IntegerField()
    product_brand = models.CharField(max_length = 30)
    product_image = models.ImageField(upload_to ='shop')
    
    def __str__(self):
        return  f'{self.user.get_full_name()},{self.product_name}'