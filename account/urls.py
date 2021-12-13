from django.urls import path
from . import views
urlpatterns=[
    path('buyer/registration/',views.buyerRegistrationPage,name='URL_NAME_BUYER_REGISTRATION'),
    path('buyer/doregister/',views.doRegistration,name='URL_NAME_BUYER_DO_REGISTER'),
    path('buyer/login/',views.buyerDoLogin,name='URL_NAME_BUYER_DO_LOGIN'),
    path('buyer/logout/',views.buyerLogOut,name='URL_NAME_BUYER_DO_LOGOUT'),
    path('buyer/myprofile/',views.buyerProfile,name='URL_NAME_BUYER_PROFILE'),
    path('seller/',views.shop,name="seller"),
    path('seller/create_account/',views.CreateAccount,name='URL_SELLER_CREATE_ACCOUNT'),
    path('seller/login/',views.shopLogin,name='URL_SELLER_LOGIN'),
    path('seller/logout/',views.shopLogOut,name='URL_SELLER_LOGOUT')
]