# Generated by Django 2.0.2 on 2018-03-19 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0032_contact_success_form'),
        ('content', '0062_auto_20180316_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobstaticpage',
            name='success_form',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='communication.SuccessFormStatic', verbose_name='Форма при успешной отправке резюме'),
        ),
    ]
