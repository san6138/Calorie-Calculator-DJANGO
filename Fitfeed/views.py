from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from .models import Customers, Consumeditems, Category, Fooditems
from django.db.utils import IntegrityError
from caloriecalculator.settings import LOGIN_REDIRECT_URL
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.utils.decorators import method_decorator
from django.contrib import messages

# Create your views here.

# @method_decorator(login_required)
def homepagelogic(request):
    total_calories = 0
    items_consumed = 0
    calorie_limit = 2000
    total_fooditems = []
    fooditems = Consumeditems.objects.filter(user=request.user)
    for items in fooditems:
        fooditem = items.fooditem.all()
        for item in fooditem:
            total_fooditems.append(item)
            total_calories += item.calories
            items_consumed += 1
    calories_left = calorie_limit - total_calories
    context = {
        "user_name": request.user.username,
        "fooditems": total_fooditems,
        "total_calories": total_calories,
        "calories_left": calories_left,
        "items_consumed": items_consumed,
        "calorie_limit": calorie_limit,
    }
    return render(request, "Fitfeed/Frontpage.html", context)

class CustomLoginView(LoginView):
    template_name = "registration/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        some_msg = self.request.session.get("some_msg", "")
        if "some_msg" in self.request.session:
            some_msg = self.request.session["some_msg"]
            context["some_msg"] = some_msg
            del self.request.session["some_msg"]
            print(some_msg)
            context['some_msg'] = some_msg
        return context
class HomepageView(View):
    @method_decorator(login_required(login_url=LOGIN_REDIRECT_URL))
    def get(self, request):
        return homepagelogic(request)

class AvailableItemsView(View):

    def __init__(self):
        self.addform = AddFoodItemForm()
        self.consumed_form = ConsumedItemForm()

    @method_decorator(login_required(login_url=LOGIN_REDIRECT_URL))
    def get(self, request):
        available_items = Fooditems.objects.all()
        return render(request, "Fitfeed/availableitems.html", {"available_items": available_items,
                                                              "addform": self.addform,
                                                              "consumedform": self.consumed_form,
                                                              "user_name": request.user.username
                                                              })

    @method_decorator(login_required(login_url=LOGIN_REDIRECT_URL))
    def post(self, request):
        form = AddFoodItemForm(request.POST)
        if form.is_valid():
            try:
                new_item = Fooditems.objects.create(name=form.cleaned_data['name'],
                                     calories=form.cleaned_data['calories'],
                                     carbohydrates=form.cleaned_data['carbohydrates'],
                                     fats=form.cleaned_data['fats'],
                                     sugar=form.cleaned_data['sugar'],
                                     protein=form.cleaned_data['protein'])
            except IntegrityError:
                    return render(request, "Fitfeed/similar_food_item_error.html", {"user_name": request.user.username})
            new_item.category.set(form.cleaned_data['category'])
            available_items = Fooditems.objects.all()

            return render(request, "Fitfeed/availableitems.html", {"available_items": available_items,
                                                                   "addform": self.addform,
                                                                   "consumedform": self.consumed_form,
                                                                   "user_name": request.user.username})



class AddConsumedItemsView(View):
     @method_decorator(login_required(login_url=LOGIN_REDIRECT_URL))
     def post(self, request):
         form = ConsumedItemForm(request.POST)
         if form.is_valid():
             Consumed_item = Consumeditems.objects.create(user=request.user)
             Consumed_item.fooditem.set(form.cleaned_data['food_item'])
             return homepagelogic(request)

class SignUpPageView(View):

    def get(self, request):
        form = SignUpForm()
        context = {"user_name": request.user.username, "form": form }
        if "messages" in request.session:
            messages = request.session.get("messages")
            context["messages"] = messages
            del request.session["messages"]
            print(messages)
        return render(request, "registration/signupform.html", context)

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except IntegrityError:
                some_msg = "User already exists.Please try with a different username"
                request.session["some_msg"] = some_msg
                return redirect('login')
            request.session["some_msg"] = "User Successfully created. Please login."
            return redirect('login')
        else:
            error_list = []
            for err_list in form.errors.values():
                for error in err_list:
                    error_list.append(error)
            request.session["messages"] = error_list
            return redirect('signup_page')





