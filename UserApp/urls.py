from django.contrib import admin
from django.urls import path,include
#from .views import indexView,aboutView
from .views import *

urlpatterns = [
    path('',indexView),
    path('about/',aboutView)
]
