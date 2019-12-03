
from django.contrib import admin
from django.urls import path,include
from .views import  getData, getDataPage
#from .classviews import MyView

urlpatterns = [

    path ('studentdata', getData ),
    path('data', getDataPage)

]