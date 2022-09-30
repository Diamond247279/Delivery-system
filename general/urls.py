from django.urls import path
from .views import *
urlpatterns = [
  path('',homepage,name='index'),
  path('about',about,name='about_us'),
  path('services',services,name='services'),
  path('price',price,name='price'),
  path('contact',contact,name='contact'),
  path('quote',quote,name='quote'),
  path('details',details,name='details'),
  path('sign_up',sign_up,name='sign_up'),
  path('sign_in',sign_in,name='sign_in'),
  path('dashboard',dashboard,name='dashboard'),
  path('log_out',logout_page,name='log_out'),
  
]
