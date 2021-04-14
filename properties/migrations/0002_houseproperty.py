# Generated by Django 3.1.7 on 2021-04-14 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('misc', '0002_businesscenter'),
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0, verbose_name='Price')),
                ('area', models.FloatField(default=0, verbose_name='Area')),
                ('built_year', models.IntegerField(default=2000, verbose_name='Year')),
                ('exploitation_year', models.IntegerField(default=2000, verbose_name='Exploitation year')),
                ('kitchen_area', models.FloatField(default=0, verbose_name='Kitchen area')),
                ('construction_type', models.CharField(default='', max_length=100, verbose_name='Construction type')),
                ('land_area', models.FloatField(default=0, verbose_name='Land area')),
                ('number_of_floors', models.PositiveIntegerField(default=0, verbose_name='Number of floors')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misc.address', verbose_name='Address')),
                ('rooms', models.ManyToManyField(to='misc.Room', verbose_name='Rooms')),
            ],
            options={
                'verbose_name': 'House property',
                'verbose_name_plural': 'House properties',
            },
        ),
    ]