# Generated by Django 3.1.7 on 2021-04-24 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('misc', '0004_delete_room'),
        ('properties', '0006_auto_20210424_0554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commercialproperty',
            name='business_center',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='misc.businesscenter', verbose_name='Business center'),
        ),
    ]
