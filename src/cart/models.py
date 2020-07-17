from django.db import models
from django.contrib.auth import get_user_model
from book.models import BookApp

User = get_user_model()

class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='carts',
        blank = True,
        null = True
    )

    def __str__(self):
        return f'Cart {self.pk}'

class BookInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='books',
    )
    book = models.ForeignKey(
        BookApp,
        on_delete=models.CASCADE,
        related_name='book_in_cart',
    )
    quantity = models.IntegerField(
        verbose_name="Quantity",
        default=1
    )

    def __str__(self):
        return f'Book {self.book.pk} In cart {self.cart.pk}'

    def price(self):
        price = self.quantity * self.book.price
        return price

class Meta:
    unique_together = (('cart', 'book'),)