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
    list_filter = (('deanery', RelatedDropdownFilter),)
    empty_value_display = '- не задано -'
    search_fields = ('name',)


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'address', 'floors', 'year', 'wear', 'material', 'land',
    )
    list_filter = (
        ('material', RelatedDropdownFilter),
        ('picture', admin.filters.EmptyFieldListFilter)
    )
    empty_value_display = '- не задано -'
    search_fields = ('name',)
    fieldsets = (
        ('Описание здания', {'fields': ('name', 'address')}),
        ('Характеристики здания', {
            'fields': ('year', 'wear', 'material', 'floors', 'land')
        }),
        ('Дополнительные сведения', {'fields': ('picture', 'comment')}),
    )


@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = (
        'number', 'target', 'building', 'department',
        'square', 'windows', 'heaters',
    )
    list_filter = (
        ('target', RelatedDropdownFilter),
        ('department', RelatedDropdownFilter),
        ('building', RelatedDropdownFilter),
    )
    empty_value_display = '- не задано -'
    search_fields = ('number',)
    fieldsets = (
        ('Описание помещения', {'fields': ('number', 'target')}),
        ('Характеристики помещения', {
            'fields': ('square', 'windows', 'heaters')
        }),
        ('Местонахождение и принадлежность', {
            'fields': ('building', 'department')
        }),
    )


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
    list_filter = (
        ('hall', RelatedDropdownFilter),
        ('chief', RelatedDropdownFilter),
        'date_start',
    )
    empty_value_display = '- не задано -'
    search_fields = ('name',)
    fieldsets = (
        ('Описание имущества', {
            'fields': ('name', 'hall'),
        }),
        ('Бухгалтерская информация', {
            'fields': ('cost', 'date_start', 'period'),
        }),
        ('Переоценка', {
            'fields': ('cost_year', 'cost_after'),
        }),
        ('Ответственный за имущество', {'fields': ('chief',)}),
    )
