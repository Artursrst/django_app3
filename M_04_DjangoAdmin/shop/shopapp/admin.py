from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from .models import Product, Order

class OrderInline(admin.TabularInline):
    model = Product.orders.through

@admin.action(description = "Archive products")
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=True)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    actions = [
        mark_archived,
    ]
    inlines = [
        OrderInline,
    ]
    list_display = "pk", "name", "description", "price", "discount"
    list_display_links = "pk", "name",
    search_fields = "pk", "name"
    fieldsets = [
        (None,{
            "fields": ("name", "description"),
        }),
        ("Price options", {
            "fields": ("price", "discount"),
            "classes": ("collapse",),
        }),
        ("Extra options", {
            "fields": ("archived",),
            "classes": ("collapse",),
        })
    ]

class ProductInline(admin.StackedInline):
    model = Order.products.through

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
    ]
    list_display = "pk", "delivery_address", "promocode", "created_at",
    list_display_links = "pk", "delivery_address",
    search_fields = "pk", "delivery_address"