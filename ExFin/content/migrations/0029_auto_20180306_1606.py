# Generated by Django 2.0.2 on 2018-03-06 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0028_auto_20180306_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='closecredit',
            name='icon_class',
            field=models.CharField(choices=[('vg-phone', 'Терминал'), ('svg-tablet', 'Личный кабинет'), ('svg-house', 'Банк')], max_length=128, verbose_name='Иконка'),
        ),
    ]