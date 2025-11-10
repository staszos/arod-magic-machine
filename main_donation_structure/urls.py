from django.urls import path
from .views import layout, main_donation_structure
from . import views




urlpatterns = [
    path('', views.layout, name='layout'),
    path('main_donation_structure', views.main_donation_structure, name='main_donation_structure'),
    path('arod_main_FAQ', views.arod_main_FAQ, name='arod_main_FAQ'),
    

]