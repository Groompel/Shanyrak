# Generated by Django 3.1.7 on 2021-05-15 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0011_auto_20210515_0311'),
    ]

    operations = [
        migrations.AddField(
            model_name='commercialproperty',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/images', verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='flatproperty',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/images', verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='houseproperty',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/images', verbose_name='Image'),
        ),
    ]
