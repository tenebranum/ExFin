# Generated by Django 2.0.2 on 2018-03-12 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0002_auto_20180312_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='demands',
            field=models.TextField(verbose_name='Требования'),
        ),
    ]
