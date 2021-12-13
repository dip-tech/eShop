from django.db import models
from django.db.models.fields import CharField
from datetime import datetime

# Create your models here.
class Order(models.Model):
    order_id=models.CharField(primary_key=True,unique=True,max_length=20)
    items=models.CharField(max_length=5000,default='')
    user_id=models.CharField(max_length=2000,default='')
    shop_id=models.CharField(max_length=2000,default='')
    name=models.CharField(max_length=200,default='')
    email=models.CharField(max_length=100,default='')
    address=models.CharField(max_length=2000,default='')
    total_items=models.CharField(max_length=10,default='')
    total_amount=models.CharField(max_length=20,default='')
    discount=models.CharField(max_length=10,default='')
    payment_method=models.CharField(max_length=100,default='')
    order_status=models.CharField(max_length=50,default='Ordered')

class OrderTracker(models.Model):
    trackingid=models.CharField(primary_key=True,max_length=20,unique=True,default='')
    oid=models.CharField(max_length=20,null=False,default='')
    order_status=models.CharField(max_length=100,default='')
    order_status_desc=models.CharField(max_length=500,default='')
    order_datetime=models.CharField(max_length=20,default='')
    
