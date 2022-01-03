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
    if request.method=='GET':
        scode=request.GET.get('s_code','')
        return render(request,'product/update_product.html')
    return render(request,'product/update_product.html')
