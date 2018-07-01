# Generated by Django 2.0.2 on 2018-03-13 20:54

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0051_auto_20180313_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutusstatic',
            name='meta_description',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Meta description страницы'),
        ),
        migrations.AddField(
            model_name='aboutusstatic',
            name='meta_description_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Meta description страницы'),
        ),
        migrations.AddField(
            model_name='aboutusstatic',
            name='meta_description_ua',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Meta description страницы'),
        ),
        migrations.AddField(
            model_name='aboutusstatic',
            name='meta_title',
            field=models.CharField(max_length=255, null=True, verbose_name='Meta title страницы'),
        ),
        migrations.AddField(
            model_name='aboutusstatic',
            name='meta_title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Meta title страницы'),
        ),
        migrations.AddField(
            model_name='aboutusstatic',
            name='meta_title_ua',
            field=models.CharField(max_length=255, null=True, verbose_name='Meta title страницы'),
        ),
        migrations.AddField(
            model_name='aboutusstatic',
            name='title_top',
            field=models.CharField(max_length=255, null=True, verbose_name='Title страницы'),
        ),
        migrations.AddField(
            model_name='aboutusstatic',
            name='title_top_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Title страницы'),
        ),
        migrations.AddField(
            model_name='aboutusstatic',
            name='title_top_ua',
            field=models.CharField(max_length=255, null=True, verbose_name='Title страницы'),
        ),
    ]