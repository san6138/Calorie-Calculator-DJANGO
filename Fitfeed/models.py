from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Creates a user
class Customers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    date_created = models.DateField(auto_now=True)

# creates a catgory for fooditems
class Category(models.Model):
    options = (
        ('breakfast', 'breakfast'),
        ('dinner', 'dinner'),
        ('lunch', 'lunch'),
        ('snack', 'snack')
    )
    category = models.CharField(max_length=255, choices=options)

    def __str__(self):
        return self.category

# Creates a item with neccessary information.
# all the information is taken per 100g
class Fooditems(models.Model):
    name = models.CharField(max_length=255, unique=True)
    calories = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField(Category)
    carbohydrates = models.DecimalField(max_digits=5, decimal_places=2)
    fats = models.DecimalField(max_digits=5, decimal_places=2)
    sugar = models.DecimalField(max_digits=5, decimal_places=2)
    protein = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

# Keeps track food items consumed untill now for every user.
class Consumeditems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fooditem = models.ManyToManyField(Fooditems)
    quantity = models.DecimalField(max_digits=6, decimal_places=2)



