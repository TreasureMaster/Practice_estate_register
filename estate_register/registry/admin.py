from django.contrib import admin

from .models import (
    Deanery,
    # Department,
    Material,
    Target,
)

# Register your models here.

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'material')
    search_fields = ('material',)


@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    list_display = ('id', 'target')
    search_fields = ('target',)


@admin.register(Deanery)
class DeaneryAdmin(admin.ModelAdmin):
    list_display = ('id', 'deanery')
    search_fields = ('deanery',)


# @admin.register(Department)
# class DepartmentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'boss', 'phone', 'dianery')
#     search_fields = ('name', 'dianery')
