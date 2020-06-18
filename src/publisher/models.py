from django.db import models

class Publisher(models.Model):
    name = models.CharField(
        verbose_name='Название издательства',
        max_length=50
    )   
    description = models.TextField(
        verbose_name='Аннотация',
        null=True,
        blank=True
    )
    image = models.ImageField(
        verbose_name='Логотип издательства',
        upload_to='media/',
        null=True,
        blank=True
    )
    
    def __str__(self):
        return self.name