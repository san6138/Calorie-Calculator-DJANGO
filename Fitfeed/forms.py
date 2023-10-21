from django import forms
from .models import Category, Fooditems
from django.contrib.auth.models import User


# class FrontPageForm(forms.Form):
#     user = forms.CharField(max_length=100)
#     password = forms.CharField(max_length=100)

class AddFoodItemForm(forms.Form):

    name = forms.CharField(max_length=255)
    calories = forms.DecimalField(max_digits=5, decimal_places=2)
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all())
    carbohydrates = forms.DecimalField(max_digits=5, decimal_places=2)
    fats = forms.DecimalField(max_digits=5, decimal_places=2)
    sugar = forms.DecimalField(max_digits=5, decimal_places=2)
    protein = forms.DecimalField(max_digits=5, decimal_places=2)

class ConsumedItemForm(forms.Form):
    food_item = forms.ModelMultipleChoiceField(label="Food item", queryset=Fooditems.objects.all())

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
