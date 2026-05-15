from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('cars/', views.car, name='car'),
    path('cars/<int:car_id>/', views.car_detail, name='car_detail'),
    path('cars/api/', views.car_api, name='car_api'),
    path('about/', views.about, name='about'),
    path('promotions/', views.promotions, name='promotions'),
    path('contacts/', views.contacts, name='contacts'),
]