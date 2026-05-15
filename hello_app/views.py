from django.shortcuts import render, get_object_or_404
from .models import Car, Seller, CarImage, Categories
from django.http import JsonResponse

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
    return render(request, 'main.html', context)

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    car_images = car.additional_images.all()
    
    context = {
        'car': car,
        'car_images': car_images,
        'title': f'{car.name} - АвтоСалон'
    }
    return render(request, 'car_detail.html', context)

def car_api(request):
    cars = Car.objects.all()
    brand = request.GET.get('brand', '')
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')
    year = request.GET.get('year', '')
    category = request.GET.get('category', '')
    
    if brand:
        cars = [car for car in cars if car.name.startswith(brand)]
    
    if min_price:
        cars = [car for car in cars if int(car.price) >= int(min_price)]
    
    if max_price:
        cars = [car for car in cars if int(car.price) <= int(max_price)]
    
    if year:
        cars = [car for car in cars if car.year == int(year)]
    
    if category:
        cars = [car for car in cars if car.categories_id.name == category]
    
    cars_data = []
    for car in cars:
        cars_data.append({
            'id': car.id,
            'name': car.name,
            'price': car.price,
            'year': car.year,
            'equipment': car.equipment,
            'colour': car.colour,
            'category': car.categories_id.name,
            'image_url': car.image.url if car.image else '/static/image/584x438.webp',
        })
    
    return JsonResponse({'cars': cars_data, 'count': len(cars_data)})

def about(request):
    context = {
        'title': 'О компании - АвтоСалон'
    }
    return render(request, 'about.html', context)
def promotions(request):
    context = {
        'title': 'Акции - АвтоСалон'
    }
    return render(request, 'promotions.html', context)

def contacts(request):
    context = {
        'title': 'Контакты - АвтоСалон'
    }
    return render(request, 'contacts.html', context)