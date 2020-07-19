from django.db import models
from cart.models import Cart
# Create your models here.

class Order(models.Model):
    cart = models.OneToOneField(
        Cart,
        on_delete = models.PROTECT,
        related_name = "order"
    )
    status = models.BooleanField(
        "Заказ выполнен",
        default=False
    )
    delivery_address = models.TextField('Адрес доставки')
    contact_phone = models.CharField('Контактный телефон', max_length=50)
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