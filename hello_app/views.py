from django.shortcuts import render
from .models import *

def main(request):
    # Получаем параметр марки из GET-запроса
    selected_brand = request.GET.get('brand', '')
    
    # Фильтруем автомобили по марке если указана
    if selected_brand:
        cars = Car.objects.filter(name__startswith=selected_brand)
    else:
        cars = Car.objects.all()[:4]  # Только первые 4 для главной
    
    sellers = Seller.objects.all()
    
    # Получаем уникальные марки для фильтра
    brands = set(car.name.split()[0] for car in Car.objects.all() if car.name)
    
    context = {
        'cars': cars,
        'sellers': sellers,
        'brands': sorted(brands),
        'selected_brand': selected_brand,
    }
    
    return render(request, 'main.html', context)

def index2(request):
    # Получаем параметр марки из GET-запроса
    selected_brand = request.GET.get('brand', '')
    
    # Фильтруем автомобили по марке если указана
    if selected_brand:
        cars = Car.objects.filter(name__startswith=selected_brand)
    else:
        cars = Car.objects.all()
    
    # Получаем уникальные марки для фильтра
    brands = set(car.name.split()[0] for car in Car.objects.all() if car.name)
    
    context = {
        'cars': cars,
        'brands': sorted(brands),
        'selected_brand': selected_brand,
        'cars_count': cars.count(),
    }
    
    return render(request, 'index2.html', context)