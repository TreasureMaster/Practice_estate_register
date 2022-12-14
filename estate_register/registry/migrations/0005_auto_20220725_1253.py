# Generated by Django 4.0.6 on 2022-07-25 09:53

from django.db import migrations


def fill_targets(apps, schema_editor):
    """Заполнение модели Target данными"""
    targets = (
        'аудитория', 'лаборатория', 'вычислительный центр',
        'деканат', 'спортзал',
    )
    Target = apps.get_model('registry', 'Target')

    for target in targets:
        Target.objects.get_or_create(target=target)


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0004_target'),
    ]

    operations = [
        migrations.RunPython(fill_targets),
    ]
