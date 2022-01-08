from django.http.response import HttpResponseRedirect
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

def addNewProdutcs(request):
    if request.method=='POST':
        p_image=request.FILES.get('pimg')
        p_title=request.POST.get('ptitle')
        p_brand=request.POST.get('pbrand')
        p_desc=request.POST.get('pdesc')
        p_category=request.POST.get('pcategory')
        p_series=request.POST.get('pseries')
        p_price=request.POST.get('pprice')
        p_soldby=request.POST.get('psoldby')
        NEW_PRODUCT=EshopProducts.objects.create(PRODUCT_BRAND=p_brand,PRODUCT_TITLE=p_title,
                    PRODUCT_DESC=p_desc,PRODUCT_CATEGORY=p_category,PRODUCT_SERIES=p_series,PRODUCT_PRICE=p_price,SOLD_BY=p_soldby)
        NEW_PRODUCT.PRODUCT_IMAGE=p_image
        NEW_PRODUCT.save()
        return render(request,'product/success_message.html',{'message':'New Product Added Successfully'})

def updateProduct(request):
    try:
        if request.session['SHOP_ID']!=None:
            scode=request.GET.get('s_code','')
            pid=request.GET.get('p_id')
            item=EshopProducts.objects.get(id=pid)
            if scode=='':
                item_info={
                    'id':item.id,
                    'img':item.PRODUCT_IMAGE,
                    'brand':item.PRODUCT_BRAND,
                    'title':item.PRODUCT_TITLE,
                    'desc':item.PRODUCT_DESC,
                    'category':item.PRODUCT_CATEGORY,
                    'series':item.PRODUCT_SERIES,
                    'price':item.PRODUCT_PRICE
                }
                return render(request,'product/update_product.html',item_info)
            elif scode=='1':
                if request.GET.get('pimg'):
                    item.PRODUCT_IMAGE=request.GET.get('pimg')
                if request.GET.get('pbrand'):
                    item.PRODUCT_BRAND=request.GET.get('pbrand')
                if request.GET.get('ptitle'):
                    item.PRODUCT_TITLE=request.GET.get('ptitle')
                if request.GET.get('pdesc'):
                    item.PRODUCT_DESC=request.GET.get('pdesc')
                if request.GET.get('pcategory'):
                    item.PRODUCT_CATEGORY=request.GET.get('pcategory')
                if request.GET.get('pseries'):
                    item.PRODUCT_SERIES=request.GET.get('pseries')
                if request.GET.get('pprice'):
                    item.PRODUCT_PRICE=request.GET.get('pprice')
                item.save()

                return render(request,'product/success_message.html',{'message':'PRODUCT UPDATE SUCCESSFULL.'})
    except KeyError:
        return HttpResponseRedirect('/account/seller/')
    return HttpResponse("Error")

def viewProduct(request):
    try:
        if request.session['SHOP_ID']!=None:
            pid=request.GET.get('p_id')
            item=EshopProducts.objects.get(id=pid)
            return render(request,'product/view_product.html',{'item':item})     
    except KeyError:
        return HttpResponseRedirect('/account/seller/')
    return HttpResponse("Error")



    
