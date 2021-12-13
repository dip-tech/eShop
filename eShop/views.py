# I create this Views.py
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from products.models import EshopProducts
from django.views.decorators.cache import cache_control

@cache_control(no_cache=True, must_revalidate=True)
#create function for home page
def eshop_home(request):
    GET_ALL_PRODUCTS=EshopProducts.objects.all()
    BEST_SELLING_MOBILES=EshopProducts.objects.filter(PRODUCT_CATEGORY='Mobile')
    SONY_TV=list(EshopProducts.objects.filter(PRODUCT_BRAND='Sony',PRODUCT_CATEGORY='Television'))
    SAMSUNG_TV=list(EshopProducts.objects.filter(PRODUCT_BRAND='Samsung',PRODUCT_CATEGORY='Television'))
    ALL_PRODUCTS={
        'ALLPRODUCTS':GET_ALL_PRODUCTS,
        'MOBILES':BEST_SELLING_MOBILES[10:22],
        'TELEVISIONS':SONY_TV[:6]+SAMSUNG_TV[:6]
    }
    return render(request,'eshop/eshop_index.html',ALL_PRODUCTS)

#create funcetion for contact page
def eshop_contact(request):
    return render(request,'eshop/eshop_contact.html')

#Create function for about page
def eshop_about(request):
    return render(request,'eshop/eshop_about.html')