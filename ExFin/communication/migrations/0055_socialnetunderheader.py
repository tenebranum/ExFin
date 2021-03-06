# Generated by Django 2.0.2 on 2018-04-13 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0054_auto_20180410_1730'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialNetUnderHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=255, verbose_name='URL-адрес')),
                ('image', models.CharField(choices=[('twitter', 'Twitter'), ('pinterest', 'Pinterest'), ('linkedin', 'LinkedIn'), ('facebook', 'Facebook')], max_length=25, verbose_name='Иконка')),
            ],
            options={
                'verbose_name': 'Социальная сеть',
                'verbose_name_plural': 'Социальные сети под хедером',
            },
        ),
    ]
