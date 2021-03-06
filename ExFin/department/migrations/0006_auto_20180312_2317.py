# Generated by Django 2.0.2 on 2018-03-12 21:17

from django.db import migrations, models
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0005_department_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='address_ru',
            field=django_google_maps.fields.AddressField(max_length=128, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='department',
            name='address_ua',
            field=django_google_maps.fields.AddressField(max_length=128, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='department',
            name='city_ru',
            field=models.CharField(max_length=128, null=True, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='department',
            name='city_ua',
            field=models.CharField(max_length=128, null=True, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='department',
            name='schedule_ru',
            field=models.CharField(max_length=128, null=True, verbose_name='Режим работы'),
        ),
        migrations.AddField(
            model_name='department',
            name='schedule_ua',
            field=models.CharField(max_length=128, null=True, verbose_name='Режим работы'),
        ),
    ]
