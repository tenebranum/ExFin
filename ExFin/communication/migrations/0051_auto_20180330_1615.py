# Generated by Django 2.0.2 on 2018-03-30 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0050_userquestion_is_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userquestion',
            name='is_read',
            field=models.BooleanField(default=True, verbose_name='Прочитан'),
        ),
    ]
