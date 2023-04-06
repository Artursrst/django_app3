from django.urls import path
from .views import orders_list, create_order, products_list, create_product

urlpatterns = [
    path("products/", products_list, name = 'products_list'),
    path("products/create/", create_product, name = 'product_create'),
    path("orders/", orders_list, name = 'orders_list'),
    path("orders/create/", create_order, name = 'orders_create'),

]
