# Generated by Django 3.0.6 on 2020-06-18 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0004_auto_20200618_1223'),
        ('book', '0002_auto_20200618_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookapp',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='publisher.Publisher', verbose_name='Издательство'),
        ),
    ]