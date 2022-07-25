from django.db import models
from django.contrib.postgres.fields import CICharField

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Material(models.Model):
    """Материал здания"""
    name = CICharField(
        max_length=255,
        unique=True,
        verbose_name='Материал',
    )

    class Meta:
        verbose_name = 'Материал здания'
        verbose_name_plural = 'Материалы зданий'
        ordering = ('id',)

    def __str__(self):
        return self.name


class Target(models.Model):
    """Целевое назначение помещения"""
    name = CICharField(
        max_length=255,
        unique=True,
        verbose_name='Назначение помещения',
    )

    class Meta:
        verbose_name = 'Назначение помещения'
        verbose_name_plural = 'Назначения помещений'
        ordering = ('id',)

    def __str__(self):
        return self.name


class Deanery(models.Model):
    """Деканат"""
    name = CICharField(
        max_length=255,
        unique=True,
        verbose_name='Деканат',
    )

    class Meta:
        verbose_name = 'Деканат'
        verbose_name_plural = 'Деканаты'
        ordering = ('id',)

    def __str__(self):
        return self.name


# class Department(models.Model):
#     """Департамент, к которому относится помещение"""
#     name = CICharField(
#         max_length=255,
#         unique=True,
#         verbose_name='Департамент',
#     )
#     boss = models.CharField(
#         max_length=60,
#         verbose_name='Директор',
#     )
#     phone = PhoneNumberField(
#         unique=True,
#         null=True, blank=True,
#         verbose_name='Телефон',
#     )
#     deanery = models.CharField(
#         max_length=60,
#         verbose_name='Деканат',
#     )

#     class Meta:
#         verbose_name = 'Депарамент'
#         verbose_name_plural = 'Департаменты'
#         ordering = ('id',)

#     def __str__(self):
#         self.name
