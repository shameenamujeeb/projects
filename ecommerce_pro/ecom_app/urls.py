from django.contrib import admin
from django.urls import path, include
app_name='ecom_app'

from. import views

urlpatterns = [

    path('', views.allProductCat,name='allProductCat'),
    path('<slug:cat_slug>/',views.allProductCat,name='product_by_category'),
    path('<slug:c_slug>/<slug:pr_slug>/',views.proDetail,name='proDetail'),

]