from django.urls import path
from . import views
urlpatterns=[
    path('',views.shopHome,name="shopHome"),
    path('shop-cart/<str:uid>',views.shoppingCart,name="shopCart"),
    path('apple/',views.shopApple,name="shopApple"),
    path('samsung/',views.shopSamsung,name="shopSamsung"),
    path('sony/',views.shopSony,name="shopSony"),
    path('asus/',views.shopAsus,name="shopAsus")
]