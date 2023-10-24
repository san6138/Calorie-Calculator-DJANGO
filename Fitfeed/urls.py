from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import *


urlpatterns = [
     path('homepage/', HomepageView.as_view(), name='homepage'),
     path('availableitems/', AvailableItemsView.as_view(), name='available_items'),
     path('addconsumeditems/', AddConsumedItemsView.as_view(), name='addconsumed_items' ),
     path('signuppage/', SignUpPageView.as_view(), name='signup_page'),
     path('login/', CustomLoginView.as_view(), name='login'),
     path('resetpassword/', ResetPasswordView.as_view(), name='reset_password'),
     ]