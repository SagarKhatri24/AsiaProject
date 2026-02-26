from django.contrib import admin
from django.urls import path,include
#from .views import indexView,aboutView,signupView
from .views import *

urlpatterns = [
    path('',indexView,name="indexName"),
    path('about/',aboutView),
    path('signup/',signupView,name="signupName"),
    path('login/',loginView,name="loginName"),
    path('logout/',logoutView,name="logoutName"),
    path('profile/',profileView,name="profileName")
]
