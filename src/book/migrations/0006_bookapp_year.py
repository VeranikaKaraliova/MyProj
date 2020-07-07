# Generated by Django 3.0.6 on 2020-07-07 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_bookapp_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookapp',
            name='year',
            field=models.IntegerField(default=2015, max_length=4, verbose_name='Год издания'),
            preserve_default=False,
        ),
    ]