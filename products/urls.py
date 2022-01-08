# urls file for products app
from django.urls import path
from . import views
urlpatterns=[
    path('',views.productHome,name='ProductHome'),
    path('get_products/<str:category>/',views.getProducts,name='GetProducts'),
    path('product-details/<str:pid>/',views.productDetails,name='ProductDetails'),
    path('add-new-product/',views.addNewProdutcs,name="addNewProdutcs"),
    path('update-product-details/',views.updateProduct,name="updateProductDetails"),
    path('view/',views.viewProduct,name="viewProduct")
]