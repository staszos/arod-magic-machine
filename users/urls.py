from django.urls import path
from .views import home, profile, main_text, RegisterView, main_FAQ_adv

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('main_text', main_text, name='main_text'),
    path('main_FAQ_adv', main_FAQ_adv, name='main_FAQ_adv'),

   
]
