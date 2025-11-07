from django.urls import path
from .views import home, profile, main_text, RegisterView

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('main_text', main_text, name='main_text'),

   
]
