# Generated by Django 2.0.2 on 2018-02-28 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='email',
            field=models.EmailField(max_length=64, verbose_name='Электронная почта'),
        ),
    ]
