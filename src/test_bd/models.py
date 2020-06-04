from django.db import models

# Create your models here.

class Parsing(models.Model):
    ip = models.CharField(
        verbose_name='IP',
        max_length=10
    )
    name = models.CharField(
        verbose_name='Браузер',
        max_length=16
    )    
    description = models.TextField(
        verbose_name='Полный запрос',
        null=False,
        blank=False
    )
    created = models.DateTimeField(
        verbose_name="Создано",
        auto_now=False,
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name="Изменено",
        auto_now=True,
        auto_now_add=False
    )
    def __str__(self):
        return self.ip