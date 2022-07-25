from django.contrib import admin

from .models import (
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
