from django.db import models
from django.contrib.postgres.fields import CICharField

# Create your models here.

class Material(models.Model):
    """Материал здания"""
    material = CICharField(
        max_length=255,
        unique=True,
        verbose_name='Материал',
    )

    class Meta:
        verbose_name = 'Материал здания'
        verbose_name_plural = 'Материалы зданий'
        ordering = ('id',)
