from django.db import models

from publisher.models import Publisher
from testgenre.models import Genre
from authors.models import Authors


class BookApp(models.Model):
    name = models.CharField(
        verbose_name='Название книги',
        max_length=50
    )    
    image = models.ImageField(
        verbose_name='Фото книги',
        upload_to='bookapp-pics',
        null=True,
        blank=True
    )
    genre = models.ForeignKey(
        Genre, on_delete=models.PROTECT, 
        verbose_name='Жанр книги',
    )
    authors = models.ForeignKey(
        Authors, on_delete=models.PROTECT,
        verbose_name='Автор книги',
    )
    publisher = models.ForeignKey(
        Publisher, on_delete=models.PROTECT, 
        verbose_name='Издательство',
    )
    description = models.TextField(
        verbose_name='Описание книги',
        null=True,
        blank=True
    )
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2
    )
    slug = models.SlugField(max_length=200, db_index=True)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
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
        return self.name
