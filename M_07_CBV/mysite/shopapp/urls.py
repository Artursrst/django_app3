from django.urls import path

from .views import ShopIndexView, \
    GroupsListView, OrderListView, \
    ProductDetailsView, ProductsListView, \
    ProductCreateView, ProductUpdateView, \
    ProductDeleteView, OrderDetailView, \
    OrderCreateView, OrderUpdateView, OrderDeleteView

app_name = "shopapp"

urlpatterns = [
    path("", ShopIndexView.as_view(), name="index"),
    path("groups/", GroupsListView.as_view(), name="groups_list"),
    path("products/", ProductsListView.as_view(), name="products_list"),
    path("products/create/", ProductCreateView.as_view(), name="products_form"),
    path("product/<int:pk>/", ProductDetailsView.as_view(), name="product_details"),
    path("product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("product/<int:pk>/archive/", ProductDeleteView.as_view(), name="product_delete"),
    path("orders/", OrderListView.as_view(), name="orders_list"),
    path("orders/create/", OrderCreateView.as_view(), name="order_form"),
    path("orders/<int:pk>/", OrderDetailView.as_view(), name="order_details"),
    path("orders/<int:pk>/update/", OrderUpdateView.as_view(), name="order_update"),
    path("orders/<int:pk>/delete/", OrderDeleteView.as_view(), name="order_delete"),
]
