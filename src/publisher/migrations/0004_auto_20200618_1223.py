# Generated by Django 3.0.6 on 2020-06-18 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0003_auto_20200618_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='publisher-pics', verbose_name='Логотип издательства'),
        ),
    ]
