from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.cache import patch_cache_control
from .models import Order, OrderTracker
from django.contrib.auth.models import User
import random
import secrets
import string
import datetime
import json

# Create your views here.


def ConfrimOrder(request, uid):
    if uid != "":
        if request.method == "GET":
            global cartItems, name, address, discount, paymentmethod, userid
            # CONVERTING JSON TO DICTIONATY OBJECT
            cartItems = json.loads(request.GET.get("products"))
            name = request.GET.get("fullName")
            address = request.GET.get("deliveryAddress")
            discount = request.GET.get("flatDiscount")
            paymentmethod = request.GET.get("paymentMethod")
            userid = uid
            capcha = random.randrange(1111, 9999)
            data = {"capcha": str(capcha)}
            return render(request, "order/confrim_order.html", data)
    return HttpResponse("Error")


def PlaceOrder(request):
    userobj = User.objects.get(username=userid)
    for item in cartItems:
        datetimeobj = datetime.datetime.now()
        RANDOM_STRING = "".join(
            secrets.choice(string.ascii_uppercase) for i in range(5)
        )
        odi = (
            "ODI"
            + datetimeobj.strftime("%Y")
            + datetimeobj.strftime("%m")
            + datetimeobj.strftime("%d")
            + datetimeobj.strftime("%H")
            + datetimeobj.strftime("%M")
            + datetimeobj.strftime("%S")
            + RANDOM_STRING
        )
        SOLDBY = cartItems[item][4]
        ITEM_KEY = (item,)
        ITEM_VALUE = cartItems[item]
        STR_SINGLE_ITEM = dict.fromkeys(ITEM_KEY, ITEM_VALUE)
        totalitems = cartItems[item][3]
        totalamount = cartItems[item][3] * int(cartItems[item][2])
        orderobj = Order.objects.create(
            order_id=odi,
            items=json.dumps(STR_SINGLE_ITEM),
            user_id=userid,
            shop_id=SOLDBY,
            name=name,
            email=userobj.email,
            address=address,
            total_items=str(totalitems),
            total_amount=str(totalamount),
            discount=discount,
            payment_method=paymentmethod,
        )
        orderobj.save()
        RANDOM_STRING = "".join(
            secrets.choice(string.ascii_uppercase) for i in range(5)
        )
        tDATE = datetime.datetime.now()
        tid = (
            "TRCID"
            + tDATE.strftime("%Y")
            + tDATE.strftime("%m")
            + tDATE.strftime("%d")
            + tDATE.strftime("%H")
            + tDATE.strftime("%M")
            + tDATE.strftime("%S")
            + RANDOM_STRING
        )
        objOT = OrderTracker.objects.create(
            trackingid=tid,
            oid=odi,
            order_status="Ordered",
            order_status_desc="Order has been placed",
            order_datetime=tDATE,
        )
        objOT.save()
    return HttpResponseRedirect("/order/order-successfull/")


def OrderSuccesfull(request):
    return render(request, "order/order_successfull.html")


def ViewOrders(request, uid):
    ALLORDERS = Order.objects.filter(user_id=uid)
    orderdata = {"allorders": ALLORDERS}
    return render(request, "order/view_order.html", orderdata)


def cancelOrder(request):
    ORDER_ID = request.GET.get("orderid")
    OPTION = request.GET.get("s_code")
    ORDER_OBJECT = Order.objects.get(order_id=ORDER_ID)
    ORDER_OBJECT.order_status = "Canceled"
    ORDER_OBJECT.save()
    RANDOM_STRING = "".join(secrets.choice(string.ascii_uppercase) for i in range(5))
    tDATE = datetime.datetime.now()
    tid = (
        "TRCID"
        + tDATE.strftime("%Y")
        + tDATE.strftime("%m")
        + tDATE.strftime("%d")
        + tDATE.strftime("%H")
        + tDATE.strftime("%M")
        + tDATE.strftime("%S")
        + RANDOM_STRING
    )
    objOT = OrderTracker.objects.create(
        trackingid=tid,
        oid=ORDER_ID,
        order_status="Canceled",
        order_status_desc="Order has been canceled",
        order_datetime=tDATE,
    )
    objOT.save()
    if OPTION == "1":
        return render(request, "order/cancel_order_sh.html", {"ordid": ORDER_ID})
    else:
        return render(request, "order/cancel_order.html", {"ordid": ORDER_ID})


def UpdateTracker(request):
    if request.method == "GET":
        OPTION = request.GET.get("s_code")
        oid = request.GET.get("orderid")
        if OPTION == "0":
            oid = request.GET.get("orderid")
            getOrderObj = Order.objects.get(order_id=oid)
            ORDER_DETAILS = {"ord": getOrderObj}
            return render(request, "order/update_tracker.html", ORDER_DETAILS)
        elif OPTION == "1":
            ORD_STATUS=request.GET.get("order_status")
            ORD_STATUS_DESC=request.GET.get("order_status_desc")
            RANDOM_STRING = "".join(
                secrets.choice(string.ascii_uppercase) for i in range(5)
            )
            tDATE = datetime.datetime.now()
            tid = (
                    "TRCID"
                    + tDATE.strftime("%Y")
                    + tDATE.strftime("%m")
                    + tDATE.strftime("%d")
                    + tDATE.strftime("%H")
                    + tDATE.strftime("%M")
                    + tDATE.strftime("%S")
                    + RANDOM_STRING
                )
            objOT = OrderTracker.objects.create(
                trackingid=tid,
                oid=oid,
                order_status=ORD_STATUS,
                order_status_desc=ORD_STATUS_DESC,
                order_datetime=tDATE,
            )
            objOT.save()
            ObjOrder=Order.objects.get(order_id=oid)
            ObjOrder.order_status=ORD_STATUS
            ObjOrder.save()
            return HttpResponse("Tracker Updated for {}".format(oid))


def TrackOrder(request):
    if request.method == "GET":
        trackerOBJ = OrderTracker.objects.filter(oid=request.GET.get("orderid"))
        OPTION = request.GET.get("s_code")
        print(trackerOBJ)
        trackDATA = {"trackdatas": trackerOBJ}
        if OPTION == "1":
            return render(request, "order/track_order_sh.html", trackDATA)
        else:
            return render(request, "order/track_order.html", trackDATA)
