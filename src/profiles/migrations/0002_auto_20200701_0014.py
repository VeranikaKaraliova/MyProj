# Generated by Django 3.0.6 on 2020-06-30 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='publisher-pics', verbose_name='Фото пользователя'),
        ),
    ]