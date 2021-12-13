from django.db import models


class Buyer(models.Model):
    id=models.CharField(max_length=50,primary_key=True,unique=True,blank=False)
    house_no=models.CharField(max_length=100,default='')
    locality=models.CharField(max_length=1000,default='')
    city=models.CharField(max_length=100,default='')
    state=models.CharField(max_length=100,default='')
    zipcode=models.CharField(max_length=10,default='')

class Shop(models.Model):
    SHOP_ID=models.CharField(max_length=20,primary_key=True,unique=True)
    SHOP_NAME=models.CharField(max_length=20,default='')
    OWNER_NAME=models.CharField(max_length=50,default='')
    OWNER_MOBILE=models.CharField(max_length=10,default='')
    SHOP_HOUSE_NO=models.CharField(max_length=100,default='')
    SHOP_LOCALITY=models.CharField(max_length=1000,default='')
    SHOP_CITY=models.CharField(max_length=100,default='')
    SHOP_STATE=models.CharField(max_length=100,default='')
    SHOP_ZIP_CODE=models.CharField(max_length=10,default='')


    

    

