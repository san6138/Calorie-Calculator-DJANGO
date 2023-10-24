from django import forms
from .models import Category, Fooditems
from django.contrib.auth.models import User



class AddFoodItemForm(forms.Form):

    name = forms.CharField(max_length=255)
    calories = forms.DecimalField(max_digits=5, decimal_places=2)
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all())
    carbohydrates = forms.DecimalField(max_digits=5, decimal_places=2)
    fats = forms.DecimalField(max_digits=5, decimal_places=2)
    sugar = forms.DecimalField(max_digits=5, decimal_places=2)
    protein = forms.DecimalField(max_digits=5, decimal_places=2)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field not in ("name", "calories"):
                self.fields[f'{field}'].widget.attrs['placeholder'] = "in grams"
class ConsumedItemForm(forms.Form):
    food_item = forms.ModelMultipleChoiceField(label="Food item", queryset=Fooditems.objects.all())
    quantity = forms.DecimalField(max_digits=6, decimal_places=2,
                                  widget=forms.TextInput(attrs={'placeholder': 'in grams'}))

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['quantity'].widget.attrs['id'] = 'quantity-label'

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ResetPasswordForm(forms.Form):
    user_name = forms.CharField(label="Username", max_length=255,
                                widget=forms.TextInput(attrs={'id': 'text-1'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'id': 'text-2'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'text-3'}))
    new_password = forms.CharField(label="New password", widget=forms.PasswordInput(attrs={'id': 'text-4'}))
    confirm_password = forms.CharField(label="Confirm password", widget=forms.PasswordInput())

