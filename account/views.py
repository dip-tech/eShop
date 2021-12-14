from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth

from products.models import EshopProducts
from .models import Buyer, Shop
from order.models import Order
from django.core.signing import Signer
import random
import datetime
import secrets
import string
# Create your views here.


def buyerRegistrationPage(request):
    return render(request, 'account/buyer_registration_page.html')


def doRegistration(request):
    if request.method == 'POST':
        BUYER_FIRST_NAME = request.POST.get('bFirstName', '')
        BUYER_LAST_NAME = request.POST.get('bLastName', '')
        BUYER_USER_NAME = request.POST.get('bUserName', '')
        BUYER_EMAIL = request.POST.get('bEmailId', '')
        BUYER_PASSWORD = request.POST.get('bPassword', '')
        BUYER_HOUSE_NO = request.POST.get('bHouseNo', '')
        BUYER_LOCALITY = request.POST.get('bLocality', '')
        BUYER_CITY = request.POST.get('bCity', '')
        BUYER_STATE = request.POST.get('bState', '')
        BUYER_ZIP_CODE = request.POST.get('bZip', '')

        # encodeing BUYER_USER_NAME
        signer = Signer()
        BUYER_EN_USERNAME = signer.sign_object(BUYER_USER_NAME)

        if User.objects.filter(username=BUYER_EN_USERNAME).exists():
            return render(request, 'account/buyer_registration_page.html', {'USERNAME_TAKEN': True})
        else:
            user = User.objects.create_user(username=BUYER_EN_USERNAME, first_name=BUYER_FIRST_NAME,
                                            last_name=BUYER_LAST_NAME, email=BUYER_EMAIL, password=BUYER_PASSWORD)
            user.save()
            buyer = Buyer.objects.create(id=user.username, house_no=BUYER_HOUSE_NO,
                                         locality=BUYER_LOCALITY, city=BUYER_CITY, state=BUYER_STATE, zipcode=BUYER_ZIP_CODE)
            buyer.save()
            return render(request, "account/account_created.html") #{'username': signer.unsign_object(BUYER_USER_NAME)}


def buyerDoLogin(request):
    signer = Signer()
    user_id = signer.sign_object(request.POST.get('loginusername'))
    password = request.POST.get('loginuserpassword')
    loginuser = auth.authenticate(username=user_id, password=password)
    global SESSION_USER
    if loginuser:
        auth.login(request, loginuser)
        request.session['sessionUser'] = loginuser.first_name
        request.session['sessionUserName'] = loginuser.username
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('user not found')


def buyerLogOut(request):
    request.session['sessionUser'] = None
    request.session['sessionUserName'] = None
    auth.logout(request)
    return HttpResponseRedirect('/')


def buyerProfile(request):
    try:
        if request.session['sessionUserName'] != None:
            if request.method == 'GET':
                PROFILE_ID = request.GET.get('profile_id', '')
                PROFILE_USER_OBJ = User.objects.get(username=PROFILE_ID)
                PROFILE_BUYER_OBJ = Buyer.objects.get(id=PROFILE_ID)
                PROFILE_DATA = {
                    'USER_FIRST_NAME': PROFILE_USER_OBJ.first_name,
                    'USER_LAST_NAME': PROFILE_USER_OBJ.last_name,
                    'USER_EMAIL_ID': PROFILE_USER_OBJ.email,
                    'USER_USERID': Signer().unsign_object(PROFILE_ID),
                    'USER_HOUSE': PROFILE_BUYER_OBJ.house_no,
                    'USER_LOCALITY': PROFILE_BUYER_OBJ.locality,
                    'USER_CITY': PROFILE_BUYER_OBJ.city,
                    'USER_STATE': PROFILE_BUYER_OBJ.state,
                    'USER_ZIP': PROFILE_BUYER_OBJ.zipcode
                }
                return render(request, 'account/buyer_profile.html', PROFILE_DATA)
        else:
            return HttpResponseRedirect('/')
    except:
        return HttpResponseRedirect('/')


def shop(request):
    try:
        RANDOM_STRING = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(5))
        GENRATED_SHOP_ID = 'SH'+RANDOM_STRING+str(random.randrange(111, 999))
        if request.session['SHOP_ID'] != None:
            TOTAL_PRODUCTS=list(EshopProducts.objects.filter(SOLD_BY=request.session['SHOP_ID']))
            DELETED_PRODUCTS=list(EshopProducts.objects.filter(SOLD_BY=request.session['SHOP_ID'],IS_ACTIVE="0"))
            TOTAL_ORDERS=list(Order.objects.filter(shop_id=request.session['SHOP_ID']))
            ACTIVE_ORDERS=list(Order.objects.filter(shop_id=request.session['SHOP_ID'],order_status="Ordered"))
            SHIPPED_ORDERS=list(Order.objects.filter(shop_id=request.session['SHOP_ID'],order_status="Shipped"))
            DELIVERED_ORDERS=list(Order.objects.filter(shop_id=request.session['SHOP_ID'],order_status="Delivered"))
            CANCELED_ORDERS=list(Order.objects.filter(shop_id=request.session['SHOP_ID'],order_status="Canceled"))
            DASHBOARD_DATA={
                'RECENT_PRODUCTS':TOTAL_PRODUCTS[-10:],
                'RECENT_ORDERS':TOTAL_ORDERS[-10:],
                'TOTAL_ORDERS':len(TOTAL_ORDERS),
                'NO_OF_ACTIVE_ORDERS':len(ACTIVE_ORDERS),
                'NO_OF_SHIPPED_ORDERS':len(SHIPPED_ORDERS),
                'NO_OF_DEVIVERED_ORDERS':len(DELIVERED_ORDERS),
                'NO_OF_CANCELED_ORDERS':len(CANCELED_ORDERS),
                'NO_OF_PRODUCTS':len(TOTAL_PRODUCTS),
                'NO_OF_DELETED_PRODUCTS':len(DELETED_PRODUCTS),
                'ACTIVE_ORDERS':ACTIVE_ORDERS,
                'DELIVERED_ORDERS':DELIVERED_ORDERS,
                'CANCELED_ORDERS':CANCELED_ORDERS
            }
            return render(request, 'account/seller_dashboard.html',DASHBOARD_DATA)
        else:
            return render(request, 'account/seller_account.html', {'GN_SH_ID': GENRATED_SHOP_ID})
    except KeyError:
        return render(request, 'account/seller_account.html', {'GN_SH_ID': GENRATED_SHOP_ID})


def CreateAccount(request):
    if request.method == 'POST':
        # GET ALL THE VALUE FROM FORM
        SHOP_NAME = request.POST.get('shopname')
        OWNER_NAME = request.POST.get('ownername')
        SHOP_ID = request.POST.get('shop_id')
        OWNER_EMAIL = request.POST.get('owner_email')
        OWNER_MOBILE = request.POST.get('owner_mobile')
        SHOP_PASSWORD = request.POST.get('shop_password')
        SHOP_HOUSE_NO = request.POST.get('shop_house_or_apartment')
        SHOP_LOCALITY = request.POST.get('shop_locality')
        SHOP_CITY = request.POST.get('shop_city')
        SHOP_STATE = request.POST.get('shop_state')
        SHOP_ZIP = request.POST.get('shop_zip')

        # ENCRYPT THE USERNAME
        EN_SHOP_ID = Signer().sign_object(SHOP_ID)
        print(SHOP_ID)

        # CHECK USERNAME EXIST OR NOT
        if User.objects.filter(username=EN_SHOP_ID).exists():
            return render(request, 'account/seller_account.html', {'id_taken': True})
        else:

            SHOP_USER_OBJ = User.objects.create_user(
                username=EN_SHOP_ID, email=OWNER_EMAIL, password=SHOP_PASSWORD)
            SHOP_USER_OBJ.save()
            SHOP_OBJ = Shop.objects.create(SHOP_ID=SHOP_USER_OBJ.username, OWNER_MOBILE=OWNER_MOBILE, SHOP_HOUSE_NO=SHOP_HOUSE_NO, SHOP_NAME=SHOP_NAME,
                                           OWNER_NAME=OWNER_NAME, SHOP_LOCALITY=SHOP_LOCALITY, SHOP_CITY=SHOP_CITY, SHOP_STATE=SHOP_STATE, SHOP_ZIP_CODE=SHOP_ZIP)
            SHOP_OBJ.save()
            return render(request, 'account/seller_account_created.html', {'username': Signer().unsign_object(SHOP_USER_OBJ.username)})


def shopLogin(request):
    if request.method == 'POST':
        SHOP_ID=request.POST.get('shopid')
        SHOP_PASSWORD=request.POST.get('shoppassword')
        #ENCRYPT SHOP ID
        EN_SELLER_USERNAME= Signer().sign_object(SHOP_ID)

        #CHECK SHOP IS PRESENT IN THE SHOP ACOUNT OR NOT
        if Shop.objects.filter(SHOP_ID=EN_SELLER_USERNAME).exists():
            LOGIN_SHOP=auth.authenticate(username=EN_SELLER_USERNAME,password=SHOP_PASSWORD)
            if LOGIN_SHOP:
                auth.login(request,LOGIN_SHOP)
                SHOP_OBJECT=Shop.objects.get(SHOP_ID=LOGIN_SHOP.username)
                request.session['SHOP_NAME']=SHOP_OBJECT.SHOP_NAME
                request.session['SHOP_ID']=LOGIN_SHOP.username
                return HttpResponseRedirect('/account/seller/')
    return HttpResponse("Error While Login")

def shopLogOut(request):
    request.session['SHOP_NAME'] = None
    request.session['SHOP_ID'] = None
    auth.logout(request)
    return HttpResponseRedirect('/account/seller/')
