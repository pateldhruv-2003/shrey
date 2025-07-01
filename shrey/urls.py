from django.contrib import admin
from django.urls import path,include
from.import views
urlpatterns = [
    path('', views.index),
    path('showstudentlist',views.showstudentlist,name="showstudentlist"),
    path('showproductlist',views.showproductlist,name="showproductlist"),
]