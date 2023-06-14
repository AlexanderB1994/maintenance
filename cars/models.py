from django.db import models

class BodyType(models.Model):
    name = models.CharField(max_length=100)


class Brand(models.Model):
    name = models.CharField(max_length=100)
    body_type = models.ManyToManyField(BodyType)

class CarModel(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
#
# class Car(models.Model):
#     model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
#     year = models.IntegerField()
#     fuel_type = models.CharField(max_length=100)
#     engine = models.CharField(max_length=100)
#     fuel_consumption = models.FloatField()
#     cost_annual = models.IntegerField()
#     major_repair = models.IntegerField()
