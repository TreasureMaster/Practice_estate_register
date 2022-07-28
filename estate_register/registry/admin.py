from django.contrib import admin
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter

from .models import (
    Building,
    Chief,
    Deanery,
    Department,
    Hall,
    Material,
    Target,
    Unit,
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
    list_filter = (
        ('target', admin.filters.EmptyFieldListFilter),
        ('department', admin.filters.EmptyFieldListFilter),
        ('building', RelatedDropdownFilter),
    )
    search_fields = ('number',)


@admin.register(Chief)
class ChiefAdmin(admin.ModelAdmin):
    list_display = ('chief', 'address', 'experience')
    search_fields = ('chief',)


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'date_start', 'cost', 'period',
        'cost_year', 'cost_after', 'hall', 'chief',
    )
    # list_filter = ('hall', 'chief')
    list_filter = (
        ('hall', admin.filters.EmptyFieldListFilter),
        ('chief', admin.filters.EmptyFieldListFilter),
    )
    search_fields = ('name',)
