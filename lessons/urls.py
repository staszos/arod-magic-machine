from django.urls import path
from .views import layout, lessons1,lessons2
from . import views




urlpatterns = [
    path('', views.layout, name='layout'),
    path('lesson1', views.lessons1, name='lesson1'),
    path('lesson2', views.lessons2, name='lesson2'),
    path('target_view/', views.lessons1),
    
    path('oz_book_1', views.oz_book_1, name='oz_book_1'),
    path('oz_book_2', views.oz_book_2, name='oz_book_2'),
    path('oz_book_3', views.oz_book_3, name='oz_book_3'),
    path('oz_book_4', views.oz_book_4, name='oz_book_4'),
    path('oz_book_5', views.oz_book_5, name='oz_book_5'),
    path('oz_book_6', views.oz_book_6, name='oz_book_6'),
    path('oz_book_7', views.oz_book_7, name='oz_book_7'),
    path('oz_book_8', views.oz_book_8, name='oz_book_8'),
    path('oz_book_9', views.oz_book_9, name='oz_book_9'),
    path('oz_book_10', views.oz_book_10, name='oz_book_10'),
    path('oz_book_11', views.oz_book_11, name='oz_book_11'),
    path('oz_book_12', views.oz_book_12, name='oz_book_12'),
    path('oz_book_13', views.oz_book_13, name='oz_book_13'),
    path('oz_book_14', views.oz_book_14, name='oz_book_14'),
    path('oz_book_15', views.oz_book_15, name='oz_book_15'),
    path('oz_book_16', views.oz_book_16, name='oz_book_16'),
    path('oz_book_17', views.oz_book_17, name='oz_book_17'),
    


]