import functools

from django.db import models


class hybrid_property:
    def __init__(self, func):
        # functools.wraps(func)(self)
        self.func = func
        self.name = func.__name__
        self.exp = None

    def __get__(self, instance, owner):
        if instance is None:
            return self
        # return self.__wrapped__(instance)
        return self.func(instance)

    def expression(self, exp):
        self.exp = exp
        return self


class HybridManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset()
        for name, value in vars(qs.model).items():
            if isinstance(value, hybrid_property) and value.exp is not None:
                qs = qs.annotate(**{name: value.exp(qs.model)})
        return qs
