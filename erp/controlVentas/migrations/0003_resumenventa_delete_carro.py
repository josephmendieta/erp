# Generated by Django 4.2.11 on 2024-04-06 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlVentas', '0002_carro_delete_controlventas'),
    ]

    operations = [
        migrations.CreateModel(
            name='resumenVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreTienda', models.CharField(max_length=120)),
                ('barrioTienda', models.CharField(max_length=120)),
                ('numLocalidad', models.IntegerField()),
                ('total', models.IntegerField()),
                ('recibido', models.IntegerField()),
                ('cambio', models.IntegerField()),
                ('articulosVendidos', models.IntegerField()),
                ('fechaVenta', models.DateTimeField()),
                ('nombreVendedor', models.CharField(max_length=120)),
            ],
        ),
        migrations.DeleteModel(
            name='Carro',
        ),
    ]
