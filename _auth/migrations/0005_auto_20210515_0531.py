# Generated by Django 3.1.7 on 2021-05-15 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_auth', '0004_auto_20210416_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaultuser',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='Birth date'),
        ),
    ]
