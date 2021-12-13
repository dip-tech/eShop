
from django.contrib import admin
from . import models
#set title for Admin page
admin.site.site_title="eShop | Admin Panel"
#add admin for eshop_product
class EshopProductsAdmin(admin.ModelAdmin):
    list_display=('id','PRODUCT_IMAGE','PRODUCT_BRAND','PRODUCT_TITLE','PRODUCT_DESC','PRODUCT_CATEGORY','PRODUCT_SERIES','PRODUCT_PRICE')
    
# Register your models here.
admin.site.register(models.EshopProducts,EshopProductsAdmin)


