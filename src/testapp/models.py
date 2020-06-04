from django.db import models

# Create your models here.
class Genre (models.Model):
    # pk
    name = models.CharField(
        verbose_name='название жанра',
        max_length=100
    )
    description = models.TextField(
        verbose_name='описание',
        null=True,
        blank=True
    )
    def __str__(self):
        return self.name