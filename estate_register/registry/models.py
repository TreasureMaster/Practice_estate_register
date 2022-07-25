from django.db import models

# Create your models here.

class Material(models.Model):
    """Материал здания"""
    material = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Материал',
    )

    class Meta:
        verbose_name = 'Материал здания'
        verbose_name_plural = 'Материалы зданий'
        ordering = ('id',)
