# Generated by Django 4.2.11 on 2024-04-05 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlVentas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=120)),
                ('cantidad', models.IntegerField()),
                ('pais', models.CharField(max_length=120)),
            ],
        ),
        migrations.DeleteModel(
            name='controlVentas',
        ),
    ]
