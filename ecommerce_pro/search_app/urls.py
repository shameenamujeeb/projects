from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
app_name='search_app'

urlpatterns = [
    path('', views.SearchResult,name='SearchResult'),

]