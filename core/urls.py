from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', list_item, name='list-item'), 
    path('product/', product_page, name='product'),
    path('checkout/', checkout_page, name='checkout')
]
