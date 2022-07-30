# Generated by Django 4.0.6 on 2022-07-28 15:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0022_alter_building_material_alter_department_deanery_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='year',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1600), django.core.validators.MaxValueValidator(2022)], verbose_name='Год постройки'),
        ),
    ]