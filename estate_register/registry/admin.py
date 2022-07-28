from django.contrib import admin

from .models import (
    Building,
    Deanery,
    Department,
    Hall,
    Material,
    Target,
)

# Register your models here.

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Deanery)
class DeaneryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'boss', 'phone', 'deanery')
    list_filter = ('deanery',)
    search_fields = ('name',)


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'address', 'floors', 'year', 'wear', 'material', 'land'
    )
    list_filter = ('material',)
    search_fields = ('name',)


@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = (
        'number', 'target', 'building', 'department',
        'square', 'windows', 'heaters',
    )
    list_filter = ('building',)
    search_fields = ('number',)
