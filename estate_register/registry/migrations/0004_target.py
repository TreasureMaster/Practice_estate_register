# Generated by Django 4.0.6 on 2022-07-25 09:51

import django.contrib.postgres.fields.citext
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0003_alter_material_material'),
    ]

    operations = [
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', django.contrib.postgres.fields.citext.CICharField(max_length=255, unique=True, verbose_name='Назначение помещения')),
            ],
            options={
                'verbose_name': 'Назначение помещения',
                'verbose_name_plural': 'Назначения помещений',
                'ordering': ('id',),
            },
        ),
    ]
