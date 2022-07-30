import json

from django.core import serializers
from django.core.exceptions import ValidationError
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import View

# Для тестов из Postman нужно убрать CSRF
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import (
    Material,
)

# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class MaterialListView(View):
    def get(self, request):

        return JsonResponse({
            'materials': serializers.serialize(
                'python',
                Material.objects.all(),
                # fields=('name',),
            ),
        })

    def post(self, request):
        if not (data := request.body) or not (material := json.loads(data)):
            return JsonResponse(
                {'error': 'Ничего не передано'},
                status=400,
            )
        try:
            material = Material(**material)
            material.full_clean()
        except (TypeError, ValidationError) as e:
            del material
            return JsonResponse(
                {'error': str(e)},
                status=400,
            )
        else:
            material.save()

        return JsonResponse(
            model_to_dict(material),
            # serializers.serialize('python', [model_to_dict(material)]),
            status=201
        )


@method_decorator(csrf_exempt, name='dispatch')
class MaterialView(View):
    def get(self, request, pk):
        material = Material.objects.filter(pk=pk)
        if not material:
            return JsonResponse(
                {'error': f'Запись с id={pk} не существует'},
                status=404,
            )

        return JsonResponse({
            'material': serializers.serialize('python', material,),
        })

    def patch(self, request, pk):
        material = Material.objects.get(pk=pk)
        if not material:
            return JsonResponse(
                {'error': f'Запись с id={pk} не существует'},
                status=404,
            )
        if not (data := request.body) or not (json_data := json.loads(data)):
            return JsonResponse(
                {'error': 'Ничего не передано'},
                status=400,
            )
        if (extra_keys :=
            (set(json_data.keys()) - set(material.get_self_field_names()))
        ):
            return JsonResponse(
                {'error': f'Лишние поля: {", ".join(extra_keys)}'},
                status=400,
            )
        try:
            for fieldname in json_data.keys():
                setattr(material, fieldname, json_data[fieldname])
            material.full_clean()
        except (AttributeError, ValidationError) as e:
            del material
            return JsonResponse(
                {'error': str(e)},
                status=400,
            )
        else:
            material.save()

        return JsonResponse(model_to_dict(material))

    def delete(self, request, pk):
        material = Material.objects.filter(pk=pk)
        if not material:
            return JsonResponse(
                {'error': f'Запись с id={pk} не существует'},
                status=404,
            )

        try:
            material.delete()
        except Exception as e:
            del material
            return JsonResponse(
                {'error': str(e)},
                status=500,
            )

        return HttpResponse(status=204)
