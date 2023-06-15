from django.db import models


class BodyType(models.Model):
    name = models.CharField(max_length=100)


class Brand(models.Model):
    name = models.CharField(max_length=100)
    body_type = models.ManyToManyField(BodyType)


class CarModel(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)


class Car(models.Model):
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    year = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    engine = models.IntegerField()
    fuel_consumption = models.FloatField()
    cost_annual = models.FloatField()
    major_repair = models.FloatField()
