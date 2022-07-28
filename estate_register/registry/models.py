import datetime as dt

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
        null=True, blank=True,
        verbose_name='Деканат',
        related_name='departments',
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = 'Депарамент'
        verbose_name_plural = 'Департаменты'
        ordering = ('id',)

    def __str__(self):
        return self.name


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
        null=True, blank=True,
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
        null=True, blank=True,
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
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='halls',
        verbose_name='Назначение помещения',
    )
    department = models.ForeignKey(
        Department,
        null=True, blank=True,
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


class Chief(models.Model):
    """Ответственные за имущество"""
    chief = models.CharField(
        max_length=60,
        verbose_name='Ответственный за имущество',
    )
    address = models.CharField(
        max_length=255,
        verbose_name='Адрес проживания',
    )
    experience = models.PositiveSmallIntegerField(
        verbose_name='Опыт (лет)',
        default=0,
    )

    class Meta:
        verbose_name = 'Ответственный за имущество'
        verbose_name_plural = 'Ответственные за имущество'
        ordering = ('id',)

    def __str__(self):
        return self.chief


class Unit(models.Model):
    """Имущество"""
    name = models.CharField(
        max_length=120,
        verbose_name='Имущество',
    )
    date_start = models.DateField(
        verbose_name='Постановка на учет',
        default=dt.date.today,
    )
    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Стоимость',
    )
    cost_year = models.PositiveSmallIntegerField(
        verbose_name='Год переоценки',
        null=True, blank=True,
    )
    cost_after = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True, blank=True,
        verbose_name='Стоимость после переоценки',
    )
    period = models.PositiveSmallIntegerField(
        verbose_name='Срок службы',
    )
    hall = models.ForeignKey(
        Hall,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='units',
        verbose_name='Помещение',
    )
    chief = models.ForeignKey(
        Chief,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='units',
        verbose_name='Ответственный',
    )

    class Meta:
        verbose_name = 'Имущество'
        verbose_name_plural = 'Имущество'
        ordering = ('id',)

    def __str__(self):
        return self.name
