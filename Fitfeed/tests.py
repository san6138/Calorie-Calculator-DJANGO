from django.test import TestCase
from Fitfeed.models import Fooditems, Category, Customers, Consumeditems
from django.contrib.auth import get_user_model

# Create your tests here.
#set DJANGO_SETTINGS_MODULE = "Caloriecalculator.settings"

class TestModels(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="sangeeth", password="1234")
        self.protein_shake = Fooditems.objects.create(name="protein shake", calories=255,
                                                 carbohydrates=15, fats=4, sugar=1, protein=25)
        self.snack = Category.objects.create(category="snack")
        self.protein_shake.category.add(self.snack)
    def test_fooditems_category(self):
        self.assertIn(self.snack, self.protein_shake.category.all())

    def test_consumer_with_user_model(self):
        customer = Customers.objects.create(user=self.user, name="Sangeeth")
        self.assertEqual(self.user, customer.user)

    def test_consumed_items(self):
        customer = Customers.objects.create(user=self.user, name="Sangeeth")
        consumed_item = Consumeditems.objects.create(user=customer)
        consumed_item.fooditem.add(self.protein_shake)
        self.assertEqual(customer, consumed_item.user)
        self.assertIn(self.protein_shake, consumed_item.fooditem.all())







