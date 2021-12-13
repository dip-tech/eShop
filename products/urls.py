# urls file for products app
from django.urls import path
from . import views
urlpatterns=[
    path('',views.productHome,name='ProductHome'),
    path('get_products/<str:category>/',views.getProducts,name='GetProducts'),
    path('product-details/<str:pid>/',views.productDetails,name='ProductDetails')
]