from django.contrib import admin
from .models import Order
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display=('order_id','items','user_id','name','total_amount','payment_method')

admin.site.register(Order,OrderAdmin)
