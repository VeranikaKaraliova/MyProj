from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profiles(models.Model):
    user = models.OneToOneField(
        User,
        on_delete = models.PROTECT,
        null=True,
        blank=True
    )
    image = models.ImageField(
        verbose_name='Фото пользователя',
        upload_to='publisher-pics',
        null=True,
        blank=True
    )
    
    def __str__(self):
        return self.user