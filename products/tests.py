from django.test import TestCase

from products.models import Product, ProductCategory


class ProductTestCase(TestCase):
    def setUp(self):
        category = ProductCategory.objects.create(name="Product_category")
        self.product_1 = Product.objects.create(name="Product_1",
                                                category=category,
                                                price=1999.5,
                                                quantity=150)

        self.product_2 = Product.objects.create(name="Product_2",
                                                category=category,
                                                price=2998.1,
                                                quantity=125,
                                                is_active=False)

        self.product_3 = Product.objects.create(name="Product_3",
                                                category=category,
                                                price=998.1,
                                                quantity=115)

    def test_product_get(self):
        product_1 = Product.objects.get(name="Product_1")
        product_2 = Product.objects.get(name="Product_2")
        self.assertEqual(product_1, self.product_1)
        self.assertEqual(product_2, self.product_2)

    def test_product_print(self):
        product_1 = Product.objects.get(name="Product_1")
        product_2 = Product.objects.get(name="Product_2")
        self.assertEqual(str(product_1), 'Product_1')
        self.assertEqual(str(product_2), 'Product_2')

