from string import ascii_letters
from random import choices

from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Permission
from django.test import TestCase
from django.urls import reverse

from .models import Product, Order



class OrderDetailViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        permission_view_order = Permission.objects.get(
            codename='view_order'
        )
        cls.usertest = User.objects.create_user(username="Bob", password="qwerty")
        cls.usertest.user_permissions.add(permission_view_order)

    def setUp(self) -> None:
        self.client.force_login(self.usertest)
        self.producttest = Product.objects.create(
            name = "Phone",
            description = "Good",
            price = "3337",
            discount = "10",
            archived = False
        )
        self.producttest.created_by.add(self.usertest)
        self.ordertest = Order.objects.create(
            delivery_address="Ul. Pushkina 99",
            promocode = 'tuctuctuc',
            user = self.usertest,
            products = self.producttest,
        )
    @classmethod
    def tearDownClass(cls):
        cls.usertest.delete()

    def tearDown(self) -> None:
        self.producttest.delete()
        self.ordertest.delete()

    def test_order_detail(self):
        response = self.client.get(
            reverse("shopapp:order_details", kwargs={"pk", self.ordertest.pk})
        )
        orders = Order.objects.all()
        context_ = response.context["object"]
        for p, p_ in zip(orders, context_):
            self.assertEqual(p.pk, p_.pk)


class ProductsExportViewTestCase(TestCase):
    fixtures = [
        'products-fixture.json',
        ]

    def test_get_products_view(self):
        response = self.client.get(
            reverse("shopapp:products-export")
        )
        self.assertEqual(response.status_code, 200)
        products = Product.objects.order_by("pk").all()
        expected_data = [
            {
                'pk': product.pk,
                'name': product.name,
                'price': str(product.price),
                'archived': product.archived,
            }
            for product in products
        ]
        products_data = response.json()
        self.assertEqual(
            products_data["products"],
            expected_data,
        )
