from django.test import TestCase
from django.contrib.auth.models import User
from store.models import Category, Product

class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name='product', slug='product')

    def test_category_model_input(self):
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_return_name(self):
        data = self.data1
        self.assertEqual(str(data), 'product')

class TestProductModel(TestCase):
    def setUp(self):
        Category.objects.create(name='product', slug='product')
        self.data1 = Product.objects.create(category_id=1, title='Introduction to Python', created_by_id=1, slug='introduction-to-python', price='29.99', image='introduction_py.png')

    def test_products_model_input(self):
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'Introduction to Python')
        
