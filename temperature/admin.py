from django.contrib import admin
from . import models
# Register your models here.

class CountryAdmin(admin.ModelAdmin):
    list_display=["__str__"]
    class Meta:
        model=models.Country

class YearAdmin(admin.ModelAdmin):
    list_display=["__str__"]
    class Meta:
        model=models.Year

class MaxTempAdmin(admin.ModelAdmin):
    list_display=["__str__",'cid','jan','feb','mar','apr','may','jun','jul','aug','sep','octu','nov','dec']
    class Meta:
        model=models.MaxTemp
        
class MinTempAdmin(admin.ModelAdmin):
    list_display=["__str__",'cid','jan','feb','mar','apr','may','jun','jul','aug','sep','octu','nov','dec']
    class Meta:
        model=models.MinTemp

class MeanTempAdmin(admin.ModelAdmin):
    list_display=["__str__",'cid','jan','feb','mar','apr','may','jun','jul','aug','sep','octu','nov','dec']
    class Meta:
        model=models.MeanTemp

class SunshineAdmin(admin.ModelAdmin):
    list_display=["__str__",'cid','jan','feb','mar','apr','may','jun','jul','aug','sep','octu','nov','dec']
    class Meta:
        model=models.Sunshine

class RainfallAdmin(admin.ModelAdmin):
    list_display=["__str__",'cid','jan','feb','mar','apr','may','jun','jul','aug','sep','octu','nov','dec']
    class Meta:
        model=models.Rainfall


admin.site.register(models.Country,CountryAdmin)
admin.site.register(models.Year,YearAdmin)
admin.site.register(models.MaxTemp,MaxTempAdmin)
admin.site.register(models.MinTemp,MinTempAdmin)
admin.site.register(models.MeanTemp,MeanTempAdmin)
admin.site.register(models.Sunshine,SunshineAdmin)
admin.site.register(models.Rainfall,RainfallAdmin)

