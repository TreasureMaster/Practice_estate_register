import json
import typing as t

from django.core import serializers
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db.models import QuerySet, ForeignKey
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.template.defaultfilters import pluralize
from django.views import View

# Для тестов из Postman нужно убрать CSRF
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import (
    Building,
    Deanery,
    Department,
    Hall,
    Material,
    Target,
)

# Create your views here.

class ResponseSelectionMixin:
    """."""
    def get_json_response(
        self,
        qs: QuerySet,
        status: int = 200,
    ):
        """Возврат ответа в JSON-виде"""
        return JsonResponse(
            dict.fromkeys(
                [
                    f'{self._model.get_model_name()}'
                    f'{pluralize(len(qs))}'
                ],
                # serializers.serialize('python', entries,)
                [e for e in qs.values()]
            ),
            status=status,
        )


@method_decorator(csrf_exempt, name='dispatch')
class BaseListResource(View, ResponseSelectionMixin):
    def get(self, request):
        qs = self._model.objects.all()

        return self.get_json_response(qs)

    def post(self, request):
        entry = None
        if not (data := request.body) or not (json_data := json.loads(data)):
            return JsonResponse(
                {'error': 'Ничего не передано'},
                status=400,
            )
        try:
            json_data = self._model.get_related_fields_objs(json_data)
            entry = self._model(**json_data)
            entry.full_clean()
        except ObjectDoesNotExist as e:
            return JsonResponse(
                {'error': str(e)},
                status=400,
            )
        except TypeError as e:
            return JsonResponse(
                {'error': str(e)},
                status=400,
            )
        except ValidationError as e:
            return JsonResponse(
                {'error': e.message_dict},
                status=400,
            )
        else:
            entry.save()
            # Небольшой костыль для обхода ошибок сериализации.
            # Встроенные сериализаторы не работают с некоторыми полями.
            # Это более простая альтернатива кастомной сериализации этих полей.
            qs = self._model.objects.filter(pk=entry.pk)

        return self.get_json_response(qs, status=201)


@method_decorator(csrf_exempt, name='dispatch')
class BaseResource(View, ResponseSelectionMixin):
    def get(self, request, pk):
        qs = self._model.objects.filter(pk=pk)

        if not qs:
            return JsonResponse(
                {'error': f'Запись с id={pk} не существует'},
                status=404,
            )

        return self.get_json_response(qs)

    def patch(self, request, pk):
        qs = self._model.objects.filter(pk=pk)
        if not qs:
            return JsonResponse(
                {'error': f'Запись с id={pk} не существует'},
                status=404,
            )
        else:
            entry = qs[0]

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
            json_data = self._model.get_related_fields_objs(json_data)
            for fieldname in json_data.keys():
                setattr(entry, fieldname, json_data[fieldname])
            entry.full_clean()
        except ObjectDoesNotExist as e:
            return JsonResponse(
                {'error': str(e)},
                status=400,
            )
        except AttributeError as e:
            return JsonResponse({'error': str(e)}, status=400)
        except ValidationError as e:
            return JsonResponse({'error': e.message_dict}, status=400)
        else:
            entry.save()
            qs = self._model.objects.filter(pk=entry.pk)

        return self.get_json_response(qs)

    def delete(self, request, pk):
        qs = self._model.objects.filter(pk=pk)
        if not qs:
            return JsonResponse(
                {'error': f'Запись с id={pk} не существует'},
                status=404,
            )

        try:
            qs.delete()
        except Exception as e:
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


class DepartmantListResource(BaseListResource):
    _model = Department


class DepartmentResource(BaseResource):
    _model = Department


class BuildingListResource(BaseListResource):
    _model = Building


class BuildingResource(BaseResource):
    _model = Building


class HallListResource(BaseListResource):
    _model = Hall


class HallResource(BaseResource):
    _model = Hall
