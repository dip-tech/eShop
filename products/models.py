from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class EshopProducts(models.Model):
    PRODUCT_IMAGE=models.ImageField(upload_to='products_image',default='')
    PRODUCT_BRAND=models.CharField(max_length=50,default='')
    PRODUCT_TITLE=models.CharField(max_length=100,default='')
    PRODUCT_DESC=RichTextField(blank=True,null=True,default='')
    PRODUCT_CATEGORY=models.CharField(max_length=100,default='')
    PRODUCT_SERIES=models.CharField(max_length=100,default='')
    PRODUCT_PRICE=models.CharField(max_length=10,default='')
    SOLD_BY=models.CharField(max_length=200,default='')
    IS_ACTIVE=models.CharField(max_length=10,default="1")
    