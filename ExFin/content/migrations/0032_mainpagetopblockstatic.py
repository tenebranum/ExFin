# Generated by Django 2.0.2 on 2018-03-06 14:58

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0031_auto_20180306_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainPageTopBlockStatic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', ckeditor.fields.RichTextField(verbose_name='Заголовок')),
                ('subtitle', ckeditor.fields.RichTextField(verbose_name='Подзаголовок')),
                ('image', models.ImageField(upload_to='main_top_block', verbose_name='Картинка на заднем фоне')),
            ],
            options={
                'verbose_name_plural': 'Блок вверху главной страницы',
                'verbose_name': 'Блок',
            },
        ),
    ]
