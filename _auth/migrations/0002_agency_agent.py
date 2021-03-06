# Generated by Django 3.1.7 on 2021-04-15 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=250, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('defaultuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='_auth.defaultuser')),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='_auth.agency')),
            ],
            bases=('_auth.defaultuser',),
        ),
    ]
