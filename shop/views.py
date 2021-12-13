from django.http.response import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from products.models import EshopProducts
from django.views.decorators.cache import cache_control
from account.models import Buyer
from django.contrib.auth.models import User

@cache_control(no_cache=True, must_revalidate=True)
# Create your views here.
def shopHome(request):
    return HttpResponseRedirect('/')


def shopApple(request):

    IPHONES = EshopProducts.objects.filter(PRODUCT_BRAND='Apple', PRODUCT_CATEGORY='Mobile')
    MACBOOKS = EshopProducts.objects.filter(PRODUCT_BRAND="Apple", PRODUCT_CATEGORY='Laptop')
    IPADS = EshopProducts.objects.filter(PRODUCT_BRAND="Apple", PRODUCT_CATEGORY='Tablet')
    return render(request, 'shop/shop_apple.html', {'iphones': IPHONES, 'macbooks': MACBOOKS, 'ipads': IPADS})

def shopSamsung(request):
    GALAXY_Z_SERIES=EshopProducts.objects.filter(PRODUCT_BRAND='Samsung',PRODUCT_SERIES='Z Series',PRODUCT_CATEGORY='Mobile')
    GALAXY_S_SERIES=EshopProducts.objects.filter(PRODUCT_BRAND='Samsung',PRODUCT_SERIES='S Series',PRODUCT_CATEGORY='Mobile')
    GALAXY_NOTE_SERIES=EshopProducts.objects.filter(PRODUCT_BRAND='Samsung',PRODUCT_SERIES='Note Series',PRODUCT_CATEGORY='Mobile')
    GALAXY_A_SERIES=EshopProducts.objects.filter(PRODUCT_BRAND='Samsung',PRODUCT_SERIES='A Series',PRODUCT_CATEGORY='Mobile')
    GALAXY_M_SERIES=EshopProducts.objects.filter(PRODUCT_BRAND='Samsung',PRODUCT_SERIES='M Series',PRODUCT_CATEGORY='Mobile')
    GALAXY_F_SERIES=EshopProducts.objects.filter(PRODUCT_BRAND='Samsung',PRODUCT_SERIES='F Series',PRODUCT_CATEGORY='Mobile')
    GALAXY_TAB=EshopProducts.objects.filter(PRODUCT_BRAND='Samsung',PRODUCT_CATEGORY='Tablet')
    SAMSUNG_TV=EshopProducts.objects.filter(PRODUCT_BRAND='Samsung',PRODUCT_CATEGORY='Television')
    SAMSUNG_REFRIGERATOR=EshopProducts.objects.filter(PRODUCT_BRAND='Samsung',PRODUCT_CATEGORY='Refrigerator')
    SAMSUNG_WASHING_MACHINE=EshopProducts.objects.filter(PRODUCT_BRAND='Samsung',PRODUCT_CATEGORY='Washing Machine')
    SAMSUNG_DETAILS={
        'galaxy_z_mobile':GALAXY_Z_SERIES,
        'galaxy_s_mobile':GALAXY_S_SERIES,
        'galaxy_note_mobile':GALAXY_NOTE_SERIES,
        'galaxy_a_mobile':GALAXY_A_SERIES,
        'galaxy_m_mobile':GALAXY_M_SERIES,
        'galaxy_f_mobile':GALAXY_F_SERIES,
        'galaxy_tablet':GALAXY_TAB,
        'samsung_smart_tvs':SAMSUNG_TV,
        'samsung_refrigerators':SAMSUNG_REFRIGERATOR,
        'samsung_washing_machine':SAMSUNG_WASHING_MACHINE
    }
    return render(request,'shop/shop_samsung.html',SAMSUNG_DETAILS)
def shopSony(request):
    BLUETOOTH_SPEAKER=EshopProducts.objects.filter(PRODUCT_BRAND='Sony',PRODUCT_CATEGORY='Bluetooth Speaker')
    HOME_THEATERS=EshopProducts.objects.filter(PRODUCT_BRAND='Sony',PRODUCT_CATEGORY='Home Theater')
    SONY_TELEVISIONS=EshopProducts.objects.filter(PRODUCT_BRAND='Sony',PRODUCT_CATEGORY='Television')
    SONY_DATA={
        'speaker':BLUETOOTH_SPEAKER,
        'hometheaters':HOME_THEATERS,
        'televisions':SONY_TELEVISIONS
    }
    return render(request,'shop/shop_sony.html',SONY_DATA)

def shopAsus(request):
    ROGPHONES=EshopProducts.objects.filter(PRODUCT_BRAND='Asus',PRODUCT_CATEGORY='Mobile', PRODUCT_SERIES='ROG PHONE')
    VIVOBOOKS=EshopProducts.objects.filter(PRODUCT_BRAND='Asus',PRODUCT_CATEGORY='Laptop', PRODUCT_SERIES='Vivobook')
    ZENBOOKS=EshopProducts.objects.filter(PRODUCT_BRAND='Asus',PRODUCT_CATEGORY='Laptop', PRODUCT_SERIES='Zenbook')
    ROGLAPTOPS=EshopProducts.objects.filter(PRODUCT_BRAND='Asus',PRODUCT_CATEGORY='Laptop', PRODUCT_SERIES='ROG Laptop')
    TUFLAPTOPS=EshopProducts.objects.filter(PRODUCT_BRAND='Asus',PRODUCT_CATEGORY='Laptop', PRODUCT_SERIES='TUF Laptop')
    ASUS_DATA={
        'ROGPHONES':ROGPHONES,
        'VIVOBOOKS':VIVOBOOKS,
        'ZENBOOKS':ZENBOOKS,
        'ROGLAPTOPS':ROGLAPTOPS,
        'TUFLAPTOPS':TUFLAPTOPS
    }
    return render(request,'shop/shop_asus.html',ASUS_DATA)

def shoppingCart(request,uid):
    ActiveUserName=request.POST.get('active-user','')
    if ActiveUserName!='':
        user=User.objects.filter(username=ActiveUserName)
        buyer=Buyer.objects.filter(id=ActiveUserName)
        userData={
            'buyer_firstname':user[0].first_name,
            'buyer_lastname':user[0].last_name,
            'buyer_house':buyer[0].house_no,
            'buyer_locality':buyer[0].locality,
            'buyer_city':buyer[0].city,
            'buyer_state':buyer[0].state,
            'buyer_zipcode':buyer[0].zipcode
            
        }
        return render(request, 'shop/cartpage.html',userData)
    else:
        return HttpResponseRedirect("/")


