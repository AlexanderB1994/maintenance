import json
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from cars.models import BodyType, Brand, CarModel, Car


class Command(BaseCommand):
    help = "Import products into database from a JSON file."

    def add_arguments(self, parser):
        parser.add_argument("--file", type=str, help="Absolute path to JSON file with products data.", required=True)

    def handle(self, *args, file=None, **options):
        try:
            with open(file) as json_file:
                data = json.load(json_file)
        except Exception:
            raise CommandError(f"Data in file {file} is not accessible.")

        with transaction.atomic():
            try:
                self.create_body_types(data['body_types'])
                self.create_brands(data['brands'])
                self.create_car_models(data['car_models'])
                self.create_cars(data['cars'])
            except Exception as e:
                raise CommandError(f"Error creating objects: {str(e)}")

    def create_body_types(self, body_types):
        for body_type_data in body_types:
            try:
                BodyType.objects.get(id=body_type_data['id'], name=body_type_data['name'])
            except BodyType.DoesNotExist:
                BodyType.objects.create(id=body_type_data['id'], name=body_type_data['name'])


    # def create_brands(self, brands):
    #     for brand_data in brands:
    #         brand_id = brand_data['id']
    #         brand_name = brand_data['name']
    #         body_type_id = brand_data['body_type_id']
    #         body_types = BodyType.objects.get(id=body_type_id)
    #         try:
    #             brand = Brand.objects.get(id=brand_id, name=brand_name)
    #         except Brand.DoesNotExist:
    #             brand = Brand.objects.create(id=brand_id, name=brand_name)
    #         brand.body_type.set(body_types)

    def create_brands(self, brands):
        Brand.objects.all().delete()
        for brand_data in brands:
            brand_id = brand_data['id']
            brand_name = brand_data['name']

            try:
                brand = Brand.objects.get(id=brand_id, name=brand_name)
            except Brand.DoesNotExist:
                brand = Brand.objects.create(id=brand_id, name=brand_name)

            body_type_ids = brand_data['body_type_id']
            body_types = BodyType.objects.filter(
                id__in=body_type_ids)

            brand.body_type.set(body_types)

    # def create_car_models(self, car_models):
    #     for car_model_data in car_models:
    #         car_model_id = car_model_data['id']
    #         car_model_name = car_model_data['name']
    #         brand_id = car_model_data['brand_id']
    #         try:
    #             brand = Brand.objects.get(id=brand_id)
    #         except Brand.DoesNotExist:
    #             continue
    #         try:
    #             CarModel.objects.get(id=car_model_id, name=car_model_name, brand=brand)
    #         except CarModel.DoesNotExist:
    #             CarModel.objects.create(id=car_model_id, name=car_model_name, brand=brand)

    def create_car_models(self, car_models):
        for car_model_data in car_models:
            car_model_id = car_model_data['id']
            car_model_name = car_model_data['name']
            brand_id = car_model_data['brand_id']
            body_type_id = car_model_data['body_type_id']

            try:
                brand = Brand.objects.get(id=brand_id)
            except Brand.DoesNotExist:
                continue

            try:
                body_type = BodyType.objects.get(id=body_type_id)
            except BodyType.DoesNotExist:
                continue

            try:
                car_model = CarModel.objects.get(id=car_model_id, name=car_model_name, brand=brand, body_type=body_type)
            except CarModel.DoesNotExist:
                car_model = CarModel.objects.create(id=car_model_id, name=car_model_name, brand=brand,
                                                    body_type=body_type)


    def create_cars(self, cars):
        for car_data in cars:
            car_id = car_data['id']
            year = car_data['year']
            fuel_type = car_data['fuel_type']
            engine = car_data['engine']
            fuel_consumption = car_data['fuel_consumption']
            cost_annual = car_data['cost_annual']
            major_repair = car_data['major_repair']
            car_model_id = car_data['car_model_id']
            try:
                car_model = CarModel.objects.get(id=car_model_id)
            except CarModel.DoesNotExist:
                continue
            try:
                Car.objects.get(id=car_id, model=car_model)
            except Car.DoesNotExist:
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
