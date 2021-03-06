# Generated by Django 3.0.6 on 2020-08-02 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
        ('book', '0007_auto_20200711_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookapp',
            name='authors',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='authors.Authors', verbose_name='Автор книги'),
        ),
    ]
