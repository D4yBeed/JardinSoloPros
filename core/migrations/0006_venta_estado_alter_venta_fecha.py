# Generated by Django 4.1.5 on 2023-06-20 21:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_remove_detalleventa_total_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="venta",
            name="estado",
            field=models.CharField(default="EN PREPARACION", max_length=20),
        ),
        migrations.AlterField(
            model_name="venta",
            name="fecha",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 20, 17, 31, 25, 801491)
            ),
        ),
    ]
