from django.shortcuts import render, get_object_or_404
from .models import Car, Seller

def main(request):
    cars = Car.objects.all()[:6]
    sellers = Seller.objects.all()
    all_cars = Car.objects.all()
    brands = []
    for car in all_cars:
        brand = car.name.split()[0] if car.name else "Неизвестно"
        if brand not in brands:
            brands.append(brand)
    
    context = {
        'cars': cars,
        'sellers': sellers,
        'brands': brands,
        'title': 'Главная - АвтоСалон'
    }
    return render(request, 'main.html', context)

def car(request):
    cars = Car.objects.all()
    
    all_cars = Car.objects.all()
    brands = []
    for car in all_cars:
        brand = car.name.split()[0] if car.name else "Неизвестно"
        if brand not in brands:
            brands.append(brand)
    
    selected_brand = request.GET.get('brand', '')
    
    if selected_brand:
        cars = [car for car in cars if car.name.startswith(selected_brand)]
    
    context = {
        'cars': cars,
        'brands': brands,
        'selected_brand': selected_brand,
        'cars_count': len(cars),
        'title': 'Каталог автомобилей'
    }
    return render(request, 'index2.html', context)

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    
    context = {
        'car': car,
        'title': f'{car.name} - АвтоСалон'
    }
    return render(request, 'car_detail.html', context)