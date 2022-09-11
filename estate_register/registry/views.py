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
        entries: t.Union[QuerySet, dict],
        status: int = 200,
    ):
        """Возврат ответа в JSON-виде"""
        is_queryset = isinstance(entries, QuerySet)
        return JsonResponse(
            dict.fromkeys(
                [
                    f'{self._model.get_model_name()}'
                    f'{pluralize(len(entries) if is_queryset else 1)}'
                ],
                # serializers.serialize('python', entries,)
                [e for e in entries.values()] if is_queryset else entries
            ),
            status=status,
        )


@method_decorator(csrf_exempt, name='dispatch')
class BaseListResource(View, ResponseSelectionMixin):
    def get(self, request):
        entries = self._model.objects.all()

        return self.get_json_response(entries)

    def post(self, request):
        entry = None
        if not (data := request.body) or not (json_data := json.loads(data)):
            return JsonResponse(
                {'error': 'Ничего не передано'},
                status=400,
            )
        try:
            json_data = self._model.get_related_fields_objs(json_data)
            print(json_data)
            entry = self._model(**json_data)
            entry.full_clean()
        except ObjectDoesNotExist as e:
            return JsonResponse(
                {'error': str(e)},
                status=400,
            )
        except TypeError as e:
            del entry
            return JsonResponse(
                {'error': str(e)},
                status=400,
            )
        except ValidationError as e:
            del entry
            return JsonResponse(
                {'error': e.message_dict},
                status=400,
            )
        else:
            entry.save()

        return self.get_json_response(model_to_dict(entry), status=201)


@method_decorator(csrf_exempt, name='dispatch')
class BaseResource(View, ResponseSelectionMixin):
    def get(self, request, pk):
        entry_list = self._model.objects.filter(pk=pk)

        if not entry_list:
            return JsonResponse(
                {'error': f'Запись с id={pk} не существует'},
                status=404,
            )

        return self.get_json_response(entry_list)

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
            json_data = self._model.get_related_fields_objs(json_data)
            print(json_data)
            for fieldname in json_data.keys():
                setattr(entry, fieldname, json_data[fieldname])
            entry.full_clean()
        except ObjectDoesNotExist as e:
            return JsonResponse(
                {'error': str(e)},
                status=400,
            )
        except AttributeError as e:
            del entry
            return JsonResponse({'error': str(e)}, status=400)
        except ValidationError as e:
            del entry
            return JsonResponse({'error': e.message_dict}, status=400)
        else:
            entry.save()

        return self.get_json_response(model_to_dict(entry))

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


class DepartmantListResource(BaseListResource):
    _model = Department


class DepartmentResource(BaseResource):
    _model = Department


class HallListResource(BaseListResource):
    _model = Hall


class HallResource(BaseResource):
    _model = Hall
