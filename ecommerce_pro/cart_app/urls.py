from django.contrib import admin
from django.urls import path, include
app_name='cart_app'

from. import views

urlpatterns = [
    path('add/<int:product_id>/',views.add_cart,name='add_cart'),

    path('',views.cart_detail,name='cart_detail'),
    path('remove/<int:product_id>/',views.cart_remove,name='cart_remove'),
    path('delete/<int:product_id>/',views.delete_cart_item,name='delete_cart_item')
]