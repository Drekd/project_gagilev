from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('cars/', views.index2, name='car'),
]