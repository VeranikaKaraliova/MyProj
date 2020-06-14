from django.db import models

class Authors(models.Model):
    name = models.CharField(
        verbose_name='ФИО автора',
        max_length=50
    )   
    description = models.TextField(
        verbose_name='Биография',
        null=True,
        blank=True
    )
    
    def __str__(self):
        return self.name