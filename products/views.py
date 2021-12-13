from django.shortcuts import render
from django.http import HttpResponse
from .models import EshopProducts
# Create your views here.
def productHome(request):
    return HttpResponse("Product Page for All Products")

def productDetails(request,pid):
    #try:
    SeletedProduct=EshopProducts.objects.get(id=pid)
    RelatedProduct=EshopProducts.objects.filter(PRODUCT_CATEGORY=SeletedProduct.PRODUCT_CATEGORY)

    #except:
        #return HttpResponse("No Product Found.")
    return render(request,'product/product_details.html',{'ViewProduct':SeletedProduct,'relatedProducts':RelatedProduct[:6]})

def getProducts(request,category):
    CategoryProducts=EshopProducts.objects.filter(PRODUCT_CATEGORY=category)
    data={
        'categoryproducts':CategoryProducts,
        'category':category
    }
    return render(request,'product/get_product.html',data)
