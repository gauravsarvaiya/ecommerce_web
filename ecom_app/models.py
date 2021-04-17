from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.
class UserProfile(AbstractUser):
    mobile_no = models.CharField(max_length=10 ,validators = [RegexValidator(r'^\d{10}$')])
    address = models.CharField(max_length =200)
    profile_pic = models.ImageField(upload_to = 'profile_pic')
    pin_code = models.CharField(max_length=6 ,validators =[RegexValidator(r'^\d{6}$')])
    is_shop = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name

    def get_full_name(self):
        return f"{self.first_name},{self.last_name}"
     