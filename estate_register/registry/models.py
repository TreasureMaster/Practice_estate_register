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


class Department(models.Model):
    """Департамент, к которому относится помещение"""
    name = CICharField(
        max_length=255,
        unique=True,
        verbose_name='Департамент',
    )
    boss = models.CharField(
        max_length=60,
        verbose_name='Директор',
    )
    phone = PhoneNumberField(
        unique=True,
        null=True, blank=True,
        verbose_name='Телефон',
    )
    deanery = models.ForeignKey(
        Deanery,
        null=True,
        verbose_name='Деканат',
        related_name='departments',
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = 'Депарамент'
        verbose_name_plural = 'Департаменты'
        ordering = ('id',)

    def __str__(self):
        self.name


class Building(models.Model):
    """Здание комплекса зданий"""
    name = models.CharField(
        max_length=60,
        verbose_name='Здание',
    )
    land = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Площадь участка',
    )
    address = models.CharField(
        max_length=255,
        verbose_name='Адрес',
    )
    year = models.PositiveSmallIntegerField(
        verbose_name='Год постройки',
    )
    wear = models.PositiveSmallIntegerField(
        verbose_name='Износ (%)',
    )
    floors = models.PositiveSmallIntegerField(
        verbose_name='Этажи',
    )
    picture = models.ImageField(
        verbose_name='Фото здания',
        null=True, blank=True,
        upload_to='images/%Y/%m/%m',
    )
    comment = models.TextField(
        verbose_name='Доп.сведения',
        null=True, blank=True,
    )
    material = models.ForeignKey(
        Material,
        null=True,
        on_delete=models.SET_NULL,
        related_name='buildings',
        verbose_name='Материал',
    )

    class Meta:
        verbose_name = 'Здание'
        verbose_name_plural = 'Здания'
        ordering = ('id',)

    def __str__(self):
        return self.name


class Hall(models.Model):
    """Помещение в здании"""
    number = models.PositiveSmallIntegerField(
        verbose_name='Номер помещения',
        null=True,
    )
    square = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Площадь',
    )
    windows = models.PositiveSmallIntegerField(
        verbose_name='Кол-во окон',
    )
    heaters = models.PositiveSmallIntegerField(
        verbose_name='Кол-во обогревателей',
    )
    target = models.ForeignKey(
        Target,
        null=True,
        on_delete=models.SET_NULL,
        related_name='halls',
        verbose_name='Назначение помещения',
    )
    department = models.ForeignKey(
        Department,
        null=True,
        on_delete=models.SET_NULL,
        related_name='halls',
        verbose_name='Департамент',
    )
    building = models.ForeignKey(
        Building,
        on_delete=models.CASCADE,
        related_name='halls',
        verbose_name='Здание',
    )

    class Meta:
        verbose_name = 'Помещение'
        verbose_name_plural = 'Помещения'
        ordering = ('id',)

    def __str__(self):
        return '{}{}, {}'.format(
            f'№ {self.number}, ' if self.number is not None else '',
            self.target.name if self.target is not None else 'помещение',
            self.building.name,
        )
