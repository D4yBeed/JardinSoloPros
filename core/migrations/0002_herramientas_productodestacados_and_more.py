# Generated by Django 4.2.1 on 2023-06-08 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Herramientas',
            fields=[
                ('codigo', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('detalle', models.CharField(max_length=200)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('oferta', models.BooleanField()),
                ('imagen', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProductoDestacados',
            fields=[
                ('codigo', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('detalle', models.CharField(max_length=200)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('oferta', models.BooleanField()),
                ('imagen', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='oferta',
            field=models.BooleanField(),
        ),
    ]
