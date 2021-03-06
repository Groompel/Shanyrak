# Generated by Django 3.1.7 on 2021-05-15 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0009_auto_20210515_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commercialproperty',
            name='deal_type',
            field=models.CharField(choices=[('sell', 'Sell'), ('rent', 'Rent')], default=0, max_length=5),
        ),
        migrations.AlterField(
            model_name='flatproperty',
            name='deal_type',
            field=models.CharField(choices=[('sell', 'Sell'), ('rent', 'Rent')], default=0, max_length=5),
        ),
        migrations.AlterField(
            model_name='houseproperty',
            name='deal_type',
            field=models.CharField(choices=[('sell', 'Sell'), ('rent', 'Rent')], default=0, max_length=5),
        ),
    ]
