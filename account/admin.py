from django.contrib import admin
from .models import Buyer,Shop
# Register your models here.
class BuyerAdmin(admin.ModelAdmin):
    list_display=('id','house_no','locality','city','state','zipcode')

class ShopAdmin(admin.ModelAdmin):
    list_display=('SHOP_ID','SHOP_NAME','OWNER_NAME')

admin.site.register(Buyer,BuyerAdmin)
admin.site.register(Shop,ShopAdmin)




