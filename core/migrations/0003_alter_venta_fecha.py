# Generated by Django 4.2.2 on 2023-07-06 01:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_producto_oferta_venta_detalleventa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 5, 21, 55, 1, 373025)),
        ),
    ]
