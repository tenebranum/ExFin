# Generated by Django 2.0.2 on 2018-03-13 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0053_auto_20180313_2310'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advantage',
            options={'ordering': ['order'], 'verbose_name': 'Преимущество', 'verbose_name_plural': 'Преимущества'},
        ),
        migrations.AddField(
            model_name='advantage',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Порядок'),
        ),
    ]
