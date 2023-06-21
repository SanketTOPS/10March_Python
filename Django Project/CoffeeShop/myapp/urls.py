from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
   path('',views.index),
   path('about/',views.about),
   path('contact/',views.contact),
   path('services/',views.services),
   path('gallery/',views.gallery),

]
