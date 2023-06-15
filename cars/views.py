from django.shortcuts import render, redirect
from .models import BodyType, Brand, CarModel, Car


def home(request):
    return render(request, 'home.html')


def select_body_type(request):
    body_types = BodyType.objects.all()
    if request.method == 'POST':
        selected_body_type_id = int(request.POST.get('body_type'))
        return redirect('select_brand', body_type_id=selected_body_type_id)
    return render(request, 'select_body_type.html', {'body_types': body_types})


def select_brand(request, body_type_id):
    body_type = BodyType.objects.get(pk=body_type_id)
    brands = Brand.objects.filter(body_type=body_type)
    if request.method == 'POST':
        selected_brand_id = int(request.POST.get('brand'))
        return redirect('select_model', brand_id=selected_brand_id)
    return render(request, 'select_brand.html', {'brands': brands})


def select_model(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    car_models = CarModel.objects.filter(brand=brand)
    if request.method == 'POST':
        selected_car_model_id = int(request.POST.get('car_model'))
        return redirect('select_car', model_id=selected_car_model_id)
    return render(request, 'select_model.html', {'car_models': car_models})


def select_car(request, model_id):
    car_model = CarModel.objects.get(id=model_id)
    cars = Car.objects.filter(model=car_model)
    if request.method == 'POST':
        selected_year = int(request.POST.get('year'))
        selected_fuel_type = request.POST.get('fuel_type')
        selected_engine = int(request.POST.get('engine'))
        car = cars.filter(year=selected_year, fuel_type=selected_fuel_type, engine=selected_engine).first()
        return render(request, 'car_results.html', {'car': car})
    return render(request, 'select_car.html', {'car_model': car_model, 'cars': cars})


def car_details(request):
    if request.method == 'POST':
        car_id = int(request.POST.get('car_id'))
        car = Car.objects.get(id=car_id)
        return render(request, 'car_results.html', {'car': car})
    return redirect('home')
