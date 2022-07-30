import json

from django.core import serializers
from django.core.exceptions import ValidationError
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.template.defaultfilters import pluralize
from django.views import View

# Для тестов из Postman нужно убрать CSRF
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import (
    Deanery,
    Material,
    Target,
)

# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class BaseListResource(View):
    def get(self, request):
        entries = self._model.objects.all()

        return JsonResponse(
            dict.fromkeys(
                [f'{self._model.get_model_name()}{pluralize(len(entries))}'],
                serializers.serialize('python', entries,)
            )
        )

    def post(self, request):
        entry = None
        if not (data := request.body) or not (json_data := json.loads(data)):
            return JsonResponse(
                {'error': 'Ничего не передано'},
                status=400,
            )
        try:
            entry = self._model(**json_data)
            entry.full_clean()
        except (TypeError, ValidationError) as e:
            del entry
            return JsonResponse(
                {'error': str(e)},
                status=400,
            )
        else:
            entry.save()

        return JsonResponse(
            model_to_dict(entry),
            # serializers.serialize('python', [model_to_dict(material)]),
            status=201
        )


@method_decorator(csrf_exempt, name='dispatch')
class BaseResource(View):
    def get(self, request, pk):
        entry = self._model.objects.filter(pk=pk)
        if not entry:
            return JsonResponse(
                {'error': f'Запись с id={pk} не существует'},
                status=404,
            )

        return JsonResponse(
            dict.fromkeys(
                [self._model.get_model_name()],
                serializers.serialize('python', entry,)
            )
        )

    def patch(self, request, pk):
        entry = self._model.objects.get(pk=pk)
        if not entry:
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
            (set(json_data.keys()) - set(entry.get_self_field_names()))
        ):
            return JsonResponse(
                {'error': f'Лишние поля: {", ".join(extra_keys)}'},
                status=400,
            )
        try:
            for fieldname in json_data.keys():
                setattr(entry, fieldname, json_data[fieldname])
            entry.full_clean()
        except (AttributeError, ValidationError) as e:
            del entry
            return JsonResponse(
                {'error': str(e)},
                status=400,
            )
        else:
            entry.save()

        return JsonResponse(model_to_dict(entry))

    def delete(self, request, pk):
        entry = self._model.objects.filter(pk=pk)
        if not entry:
            return JsonResponse(
                {'error': f'Запись с id={pk} не существует'},
                status=404,
            )

        try:
            entry.delete()
        except Exception as e:
            del entry
            return JsonResponse(
                {'error': str(e)},
                status=500,
            )

        return HttpResponse(status=204)


class MaterialListResource(BaseListResource):
    _model = Material


class MaterialResource(BaseResource):
    _model = Material


class TargetListResource(BaseListResource):
    _model = Target


class TargetResource(BaseResource):
    _model = Target


class DeaneryListResource(BaseListResource):
    _model = Deanery


class DeaneryResource(BaseResource):
    _model = Deanery
