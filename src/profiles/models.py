from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse_lazy

User = get_user_model()

class Profiles(models.Model):
    user = models.OneToOneField(
        User,
        on_delete = models.PROTECT,
        null=True,
        blank=True
    )
    username = models.CharField(
        verbose_name='Имя пользователя',
        max_length=15
    )
    password = models.CharField(
        verbose_name='Пароль',
        max_length=15
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=50
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=50
    )
    email = models.EmailField(verbose_name='E-mail')
    phone_number = models.IntegerField(verbose_name='Номер телефона')
    address1 = models.CharField(
        verbose_name='Адрес доставки основной',
        max_length=500
    )
    address2 = models.CharField(
        verbose_name='Адрес доставки дополнительный',
        max_length=500,
        null=True,
        blank=True
    )
    image = models.ImageField(
        verbose_name='Фото пользователя',
        upload_to='profiles-pics',
        null=True,
        blank=True
    )
     
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def get_absolute_url(self):
        return reverse_lazy("home")