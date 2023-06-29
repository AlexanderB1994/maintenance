from django.contrib import admin
from cars.models import BodyType, Brand, CarModel, Car


@admin.register(BodyType)
class BodyTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    @admin.display(description="body type")
    def get_body_type(self, obj):
        return ", ".join([str(body_type) for body_type in obj.body_type.all()])

    list_display = ("name", "get_body_type",)
    ordering = ("name",)
    search_fields = ("", "",)


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ("name", "brand", "body_type",)
    ordering = ("brand", "body_type",)
    search_fields = ("name", "brand__name", "body_type__name",)
    list_per_page = 60


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    @admin.display(description="body type")
    def get_body_type(self, obj):
        return str(obj.model.body_type)

    list_display = (
        "model", "get_body_type", "year", "engine", "fuel_type", "cost_annual", "major_repair", "fuel_consumption",)
    ordering = ("model", "model__body_type",)
    search_fields = ("model__name", "model__body_type__name",)
    list_per_page = 60
