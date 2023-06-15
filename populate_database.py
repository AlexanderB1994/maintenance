import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'maintenance.settings')
django.setup()
from cars.models import BodyType, Brand, CarModel, Car

body_types = [
    {'id': 1, 'name': 'Sedan'},
    {'id': 2, 'name': 'Hatchback'},
    {'id': 3, 'name': 'Coupe'},
    {'id': 4, 'name': 'Cabriolet'},
    {'id': 5, 'name': 'SUV (Sport Utility Vehicle)'},
    {'id': 6, 'name': 'Monovolum (MPV - Multi-Purpose Vehicle)'},
    {'id': 7, 'name': 'Crossover'},
    {'id': 8, 'name': 'Break (Station Wagon)'},
    {'id': 9, 'name': 'Pick-up'},
    {'id': 10, 'name': 'Roadster'},
    {'id': 11, 'name': 'Supersport'},
    {'id': 12, 'name': 'Monovolum'},
]

for body_type_data in body_types:
    BodyType.objects.get_or_create(id=body_type_data['id'], name=body_type_data['name'])

brands = [
    {'id': 1, 'name': 'Alfa Romeo', 'body_type_id': [1, 2, 3, 4, 5, 12]},
    {'id': 2, 'name': 'Aston Martin', 'body_type_id': [1, 3, 4]},
    {'id': 3, 'name': 'Audi', 'body_type_id': [1, 2, 3, 4, 5, 7, 8]},
    {'id': 4, 'name': 'Bentley', 'body_type_id': [1, 3, 4, 5]},
    {'id': 5, 'name': 'BMW', 'body_type_id': [1, 2, 3, 4, 5, 10]},
    {'id': 6, 'name': 'Bugatti', 'body_type_id': [11]},
    {'id': 7, 'name': 'Citroën', 'body_type_id': [1, 2, 3, 4, 5, 12]},
    {'id': 8, 'name': 'Dacia', 'body_type_id': [1, 2, 8]},
    {'id': 9, 'name': 'Ferrari', 'body_type_id': [11, 3, 4]},
    {'id': 10, 'name': 'Fiat', 'body_type_id': [1, 2, 3, 4]},
    {'id': 11, 'name': 'Jaguar', 'body_type_id': [1, 3, 4, 5]},
    {'id': 12, 'name': 'Lamborghini', 'body_type_id': [11, 3, 10, 5]},
    {'id': 13, 'name': 'Land Rover', 'body_type_id': [5, 7]},
    {'id': 14, 'name': 'Maserati', 'body_type_id': [1, 3, 4, 5]},
    {'id': 15, 'name': 'Mercedes-Benz', 'body_type_id': [1, 2, 3, 4, 5, 8]},
    {'id': 16, 'name': 'MINI', 'body_type_id': [2, 3, 4, 5]},
    {'id': 17, 'name': 'Opel', 'body_type_id': [1, 2, 3, 4, 5, 6, 8]},
    {'id': 18, 'name': 'Peugeot', 'body_type_id': [1, 2, 3, 4, 5, 8, 12]},
    {'id': 19, 'name': 'Porsche', 'body_type_id': [3, 4, 5]},
    {'id': 20, 'name': 'Renault', 'body_type_id': [1, 2, 3, 4, 5, 8, 9]},
    {'id': 21, 'name': 'Rolls-Royce', 'body_type_id': [1, 3, 4, 5]},
    {'id': 22, 'name': 'SEAT', 'body_type_id': [1, 2, 5]},
    {'id': 23, 'name': 'Škoda', 'body_type_id': [1, 2, 5, 8]},
    {'id': 24, 'name': 'Tesla', 'body_type_id': [1, 3, 5]},
    {'id': 25, 'name': 'Volkswagen', 'body_type_id': [1, 2, 3, 4, 5, 6, 8]},
    {'id': 26, 'name': 'Volvo', 'body_type_id': [1, 2, 5, 8]},
]

for brand_data in brands:
    brand_id = brand_data['id']
    brand_name = brand_data['name']
    body_type_ids = brand_data['body_type_id']
    body_types = BodyType.objects.filter(id__in=body_type_ids)
    brand, _ = Brand.objects.get_or_create(id=brand_id, name=brand_name)
    brand.body_type.set(body_types)

car_models = [
    {'id': 1, 'name': 'Alfa Romeo Giulia', 'brand_id': 1},
    {'id': 2, 'name': 'Alfa Romeo Giulietta', 'brand_id': 1},
    {'id': 3, 'name': 'Alfa Romeo 4C', 'brand_id': 1},
    {'id': 4, 'name': 'Alfa Romeo Spider', 'brand_id': 1},
    {'id': 5, 'name': 'Alfa Romeo Stelvio', 'brand_id': 1},
    {'id': 6, 'name': 'Aston Martin Rapide', 'brand_id': 2},
    {'id': 7, 'name': 'Aston Martin DB11', 'brand_id': 2},
    {'id': 8, 'name': 'Aston Martin Vantage', 'brand_id': 2},
    {'id': 9, 'name': 'Audi A4', 'brand_id': 3},
    {'id': 10, 'name': 'Audi A3', 'brand_id': 3},
    {'id': 11, 'name': 'Audi TT', 'brand_id': 3},
    {'id': 12, 'name': 'Audi A5', 'brand_id': 3},
    {'id': 13, 'name': 'Audi Q5', 'brand_id': 3},
    {'id': 14, 'name': 'Audi Q7', 'brand_id': 3},
    {'id': 15, 'name': 'Audi A6', 'brand_id': 3},
    {'id': 16, 'name': 'Bentley Flying Spur', 'brand_id': 4},
    {'id': 17, 'name': 'Bentley Continental GT', 'brand_id': 4},
    {'id': 18, 'name': 'Bentley Continental GTC', 'brand_id': 4},
    {'id': 19, 'name': 'Bentley Bentayga', 'brand_id': 4},
    {'id': 20, 'name': 'BMW 3 Series', 'brand_id': 5},
    {'id': 21, 'name': 'BMW 1 Series', 'brand_id': 5},
    {'id': 22, 'name': 'BMW 4 Series', 'brand_id': 5},
    {'id': 23, 'name': 'BMW 2 Series Convertible', 'brand_id': 5},
    {'id': 24, 'name': 'BMW X5', 'brand_id': 5},
    {'id': 25, 'name': 'BMW X6', 'brand_id': 5},
    {'id': 26, 'name': 'BMW Z4', 'brand_id': 5},
    {'id': 27, 'name': 'Bugatti Chiron', 'brand_id': 6},
    {'id': 28, 'name': 'Citroën C4', 'brand_id': 7},
    {'id': 29, 'name': 'Citroën C3', 'brand_id': 7},
    {'id': 30, 'name': 'Citroën DS3', 'brand_id': 7},
    {'id': 31, 'name': 'Citroën DS4', 'brand_id': 7},
    {'id': 32, 'name': 'Citroën C5 Aircross', 'brand_id': 7},
    {'id': 33, 'name': 'Citroën C3 Aircross', 'brand_id': 7},
    {'id': 34, 'name': 'Citroën Berlingo', 'brand_id': 7},
    {'id': 35, 'name': 'Dacia Logan', 'brand_id': 8},
    {'id': 36, 'name': 'Dacia Sandero', 'brand_id': 8},
    {'id': 37, 'name': 'Dacia Duster', 'brand_id': 8},
    {'id': 38, 'name': 'Ferrari F8 Tributo', 'brand_id': 9},
    {'id': 39, 'name': 'Ferrari 812 Superfast', 'brand_id': 9},
    {'id': 40, 'name': 'Ferrari Portofino M', 'brand_id': 9},
    {'id': 41, 'name': 'Fiat Tipo', 'brand_id': 10},
    {'id': 42, 'name': 'Fiat 500', 'brand_id': 10},
    {'id': 43, 'name': 'Fiat 124 Spider', 'brand_id': 10},
    {'id': 44, 'name': 'Jaguar XE', 'brand_id': 11},
    {'id': 45, 'name': 'Jaguar F-Type', 'brand_id': 11},
    {'id': 46, 'name': 'Jaguar E-Pace', 'brand_id': 11},
    {'id': 47, 'name': 'Jaguar F-Pace', 'brand_id': 11},
    {'id': 48, 'name': 'Lamborghini Huracán', 'brand_id': 12},
    {'id': 49, 'name': 'Lamborghini Aventador', 'brand_id': 12},
    {'id': 50, 'name': 'Lamborghini Urus', 'brand_id': 12},
    {'id': 51, 'name': 'Land Rover Range Rover', 'brand_id': 13},
    {'id': 52, 'name': 'Land Rover Range Rover Sport', 'brand_id': 13},
    {'id': 53, 'name': 'Land Rover Discovery', 'brand_id': 13},
    {'id': 54, 'name': 'Land Rover Defender', 'brand_id': 13},
    {'id': 55, 'name': 'Maserati Ghibli', 'brand_id': 14},
    {'id': 56, 'name': 'Maserati GranTurismo', 'brand_id': 14},
    {'id': 57, 'name': 'Maserati Levante', 'brand_id': 14},
    {'id': 58, 'name': 'Maserati Quattroporte', 'brand_id': 14},
    {'id': 59, 'name': 'Mercedes-Benz C-Class', 'brand_id': 15},
    {'id': 60, 'name': 'Mercedes-Benz A-Class', 'brand_id': 15},
    {'id': 61, 'name': 'Mercedes-Benz E-Class', 'brand_id': 15},
    {'id': 62, 'name': 'Mercedes-Benz S-Class', 'brand_id': 15},
    {'id': 63, 'name': 'Mercedes-Benz GLC', 'brand_id': 15},
    {'id': 64, 'name': 'Mercedes-Benz GLE', 'brand_id': 15},
    {'id': 65, 'name': 'Mercedes-Benz CLA', 'brand_id': 15},
    {'id': 66, 'name': 'MINI Cooper', 'brand_id': 16},
    {'id': 67, 'name': 'MINI Clubman', 'brand_id': 16},
    {'id': 68, 'name': 'MINI Convertible', 'brand_id': 16},
    {'id': 69, 'name': 'MINI Countryman', 'brand_id': 16},
    {'id': 70, 'name': 'Opel Insignia', 'brand_id': 17},
    {'id': 71, 'name': 'Opel Corsa', 'brand_id': 17},
    {'id': 72, 'name': 'Opel Astra', 'brand_id': 17},
    {'id': 73, 'name': 'Opel Cascada', 'brand_id': 17},
    {'id': 74, 'name': 'Opel Mokka', 'brand_id': 17},
    {'id': 75, 'name': 'Opel Grandland', 'brand_id': 17},
    {'id': 76, 'name': 'Peugeot 308', 'brand_id': 18},
    {'id': 77, 'name': 'Peugeot 208', 'brand_id': 18},
    {'id': 78, 'name': 'Peugeot 508', 'brand_id': 18},
    {'id': 79, 'name': 'Peugeot 2008', 'brand_id': 18},
    {'id': 80, 'name': 'Peugeot 3008', 'brand_id': 18},
    {'id': 81, 'name': 'Peugeot 5008', 'brand_id': 18},
    {'id': 82, 'name': 'Peugeot Rifter', 'brand_id': 18},
    {'id': 83, 'name': 'Porsche 911', 'brand_id': 19},
    {'id': 84, 'name': 'Porsche Cayman', 'brand_id': 19},
    {'id': 85, 'name': 'Porsche Macan', 'brand_id': 19},
    {'id': 86, 'name': 'Porsche Cayenne', 'brand_id': 19},
    {'id': 87, 'name': 'Renault Megane', 'brand_id': 20},
    {'id': 88, 'name': 'Renault Clio', 'brand_id': 20},
    {'id': 89, 'name': 'Renault Captur', 'brand_id': 20},
    {'id': 90, 'name': 'Renault Kadjar', 'brand_id': 20},
    {'id': 91, 'name': 'Renault Koleos', 'brand_id': 20},
    {'id': 92, 'name': 'Renault Kangoo', 'brand_id': 20},
    {'id': 93, 'name': 'Renault Trafic', 'brand_id': 20},
    {'id': 94, 'name': 'Rolls-Royce Ghost', 'brand_id': 21},
    {'id': 95, 'name': 'Rolls-Royce Wraith', 'brand_id': 21},
    {'id': 96, 'name': 'Rolls-Royce Dawn', 'brand_id': 21},
    {'id': 97, 'name': 'Rolls-Royce Cullinan', 'brand_id': 21},
    {'id': 98, 'name': 'SEAT Leon', 'brand_id': 22},
    {'id': 99, 'name': 'SEAT Ibiza', 'brand_id': 22},
    {'id': 100, 'name': 'SEAT Arona', 'brand_id': 22},
    {'id': 101, 'name': 'SEAT Ateca', 'brand_id': 22},
    {'id': 102, 'name': 'Škoda Octavia', 'brand_id': 23},
    {'id': 103, 'name': 'Škoda Fabia', 'brand_id': 23},
    {'id': 104, 'name': 'Škoda Superb', 'brand_id': 23},
    {'id': 105, 'name': 'Škoda Karoq', 'brand_id': 23},
    {'id': 106, 'name': 'Tesla Model 3', 'brand_id': 24},
    {'id': 107, 'name': 'Tesla Model S', 'brand_id': 24},
    {'id': 108, 'name': 'Tesla Model X', 'brand_id': 24},
    {'id': 109, 'name': 'Volkswagen Passat', 'brand_id': 25},
    {'id': 110, 'name': 'Volkswagen Golf', 'brand_id': 25},
    {'id': 111, 'name': 'Volkswagen Polo', 'brand_id': 25},
    {'id': 112, 'name': 'Volkswagen Tiguan', 'brand_id': 25},
    {'id': 113, 'name': 'Volkswagen Touareg', 'brand_id': 25},
    {'id': 114, 'name': 'Volkswagen Touran', 'brand_id': 25},
    {'id': 115, 'name': 'Volkswagen Caddy', 'brand_id': 25},
    {'id': 116, 'name': 'Volvo S60', 'brand_id': 26},
    {'id': 117, 'name': 'Volvo V40', 'brand_id': 26},
    {'id': 118, 'name': 'Volvo XC40', 'brand_id': 26},
    {'id': 119, 'name': 'Volvo XC60', 'brand_id': 26},
    {'id': 120, 'name': 'Volvo XC90', 'brand_id': 26},
]

for car_model_data in car_models:
    car_model_id = car_model_data['id']
    car_model_name = car_model_data['name']
    brand_id = car_model_data['brand_id']
    brand = Brand.objects.get(id=brand_id)
    car_model, _ = CarModel.objects.get_or_create(id=car_model_id, name=car_model_name, brand=brand)

cars = [
    {'id': 1, 'year': 2022, 'fuel_type': 'Gasoline', 'engine': 1999, 'fuel_consumption': 7.5, 'cost_annual': 500,
     'major_repair': 1200, 'car_model_id': 1},
    {'id': 2, 'year': 2021, 'fuel_type': 'Diesel', 'engine': 1498, 'fuel_consumption': 6.5, 'cost_annual': 300,
     'major_repair': 1900, 'car_model_id': 1},
    {'id': 3, 'year': 2019, 'fuel_type': 'Gasoline', 'engine': 3349, 'fuel_consumption': 9.5, 'cost_annual': 900,
     'major_repair': 13500, 'car_model_id': 1},
]

for car_data in cars:
    car_id = car_data['id']
    year = car_data['year']
    fuel_type = car_data['fuel_type']
    engine = car_data['engine']
    fuel_consumption = car_data['fuel_consumption']
    cost_annual = car_data['cost_annual']
    major_repair = car_data['major_repair']
    car_model_id = car_data['car_model_id']
    car_model = CarModel.objects.get(id=car_model_id)

    Car.objects.create(
        id=car_id,
        model=car_model,
        year=year,
        fuel_type=fuel_type,
        engine=engine,
        fuel_consumption=fuel_consumption,
        cost_annual=cost_annual,
        major_repair=major_repair
    )
