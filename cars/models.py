from django.db import models


class BodyType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)
    body_type = models.ManyToManyField(BodyType)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    body_type = models.ForeignKey(BodyType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    year = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    engine = models.IntegerField()
    fuel_consumption = models.FloatField()
    cost_annual = models.FloatField()
    major_repair = models.FloatField()

    def __str__(self):
        return self.model.name
