# Generated by Django 3.0.6 on 2020-07-19 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0003_auto_20200715_2036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starus', models.BooleanField(default=False, verbose_name='Заказ выполнен')),
                ('delivery_address', models.TextField(verbose_name='Адрес досавки')),
                ('contact_phone', models.CharField(max_length=50, verbose_name='Контактный телефон')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Изменено')),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='cart.Cart')),
            ],
        ),
    ]
