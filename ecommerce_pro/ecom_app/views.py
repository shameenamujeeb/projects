from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Category, Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage


# Create your views here.

def allProductCat(request,cat_slug=None):
    cat_page=None
    pro_list=None
    if cat_slug!=None:
        cat_page=get_object_or_404(Category,slug=cat_slug)
        pro_list=Product.objects.all().filter(category=cat_page,available=True)
    else:
        pro_list=Product.objects.all().filter(available=True)
    paginator=Paginator(pro_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pro=paginator.page(page)
    except (EmptyPage,InvalidPage):
        pro=paginator.page(paginator.num_pages)
    return render(request,'category.html',{'category':cat_page,'pro': pro})

def proDetail(request,c_slug,pr_slug):
    try:
        prod=Product.objects.get(category__slug=c_slug,slug=pr_slug)
    except Exception as e:
        raise e


    return render(request,'product.html',{'product':prod})
