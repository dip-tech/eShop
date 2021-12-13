from django.urls import path
from . import views
urlpatterns=[
    path('confrim-order/<str:uid>',views.ConfrimOrder,name="confrimOrder"),
    path('order-pleaced/',views.PlaceOrder,name="ordersuccessfull"),
    path('order-successfull/',views.OrderSuccesfull,name="ordersuccessfull"),
    path('myorders/<str:uid>/',views.ViewOrders,name="vieworders"),
    path('track_order/',views.TrackOrder,name="trackmyorder"),
    path('cancel_order/',views.cancelOrder,name="cancelcorder"),
    path('update_tracker/',views.UpdateTracker,name="updatetracker")
   
]