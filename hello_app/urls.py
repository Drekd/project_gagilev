from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('cars/', views.car, name='car'),
    path('cars/<int:car_id>/', views.car_detail, name='car_detail'), 
]