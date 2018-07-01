# Generated by Django 2.0.2 on 2018-03-25 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0063_jobstaticpage_success_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainpagetopblockstatic',
            name='footer_ru',
            field=models.CharField(max_length=128, null=True, verbose_name='Подзаголовок [ru]'),
        ),
        migrations.AddField(
            model_name='mainpagetopblockstatic',
            name='footer_ua',
            field=models.CharField(max_length=128, null=True, verbose_name='Подзаголовок [ua]'),
        ),
        migrations.AddField(
            model_name='mainpagetopblockstatic',
            name='subtitle_ru',
            field=models.CharField(max_length=128, null=True, verbose_name='Вторая строка заголовка [ru]'),
        ),
        migrations.AddField(
            model_name='mainpagetopblockstatic',
            name='subtitle_ua',
            field=models.CharField(max_length=128, null=True, verbose_name='Вторая строка заголовка [ua]'),
        ),
        migrations.AddField(
            model_name='mainpagetopblockstatic',
            name='title_ru',
            field=models.CharField(max_length=128, null=True, verbose_name='Первая строка заголовка [ru]'),
        ),
        migrations.AddField(
            model_name='mainpagetopblockstatic',
            name='title_ua',
            field=models.CharField(max_length=128, null=True, verbose_name='Первая строка заголовка [ua]'),
        ),
    ]