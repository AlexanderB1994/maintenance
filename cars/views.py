from django.shortcuts import render, redirect
from .models import BodyType, Brand, CarModel


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
    body_type = Brand.objects.get(id=brand_id)
    car_models = CarModel.objects.filter(brand=brand)
    if request.method == 'POST':
        selected_car_model_id = int(request.POST.get('car_model'))
        return redirect('select_car_model', model_id=selected_car_model_id)
    return render(request, 'select_model.html', {'car_models': car_models})
