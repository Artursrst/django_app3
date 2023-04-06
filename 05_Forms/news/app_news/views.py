from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, reverse

from .models import Product, Order
from .forms import ProductForm, OrderForm

def products_list(request: HttpRequest):
    context = {
        "products" : Product.objects.all(),
    }
    return render(request, 'app_news/products-form.html', context = context)

def create_product(request:HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                "products": Product.objects.all(),
            }
            return render(request, 'app_news/products-form.html', context=context)
    else:
        form = ProductForm()
    context = {
        "form": form,
    }
    return render(request, "app_news/create-product.html", context = context)

def orders_list(request: HttpRequest):
    context = {
        "orders" : Order.objects.select_related().all(),
    }
    return render(request, 'app_news/orders-form.html', context = context)

def create_order(request:HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                "orders": Order.objects.select_related().all(),
            }
            return render(request, 'app_news/orders-form.html', context=context)
    else:
        form = OrderForm()
    context = {
        "form": form,
    }
    return render(request, "app_news/create-order.html", context = context)

'''
def create_order(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            url = reverse("app_news:orders_list")
            return redirect(url)
    else:
        form = OrderForm()
    context = {
        "form" : form,
    }
    return render(request, 'app_news/create-product.html', context=context)'''