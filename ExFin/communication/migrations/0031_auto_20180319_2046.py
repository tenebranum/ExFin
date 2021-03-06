# Generated by Django 2.0.2 on 2018-03-19 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0030_successformstatic'),
    ]

    operations = [
        migrations.AddField(
            model_name='successformstatic',
            name='extra_text_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Дополнительный текст в левом нижнем углу'),
        ),
        migrations.AddField(
            model_name='successformstatic',
            name='extra_text_ua',
            field=models.CharField(max_length=255, null=True, verbose_name='Дополнительный текст в левом нижнем углу'),
        ),
        migrations.AddField(
            model_name='successformstatic',
            name='text_ru',
            field=models.TextField(max_length=400, null=True, verbose_name='Текст формы'),
        ),
        migrations.AddField(
            model_name='successformstatic',
            name='text_ua',
            field=models.TextField(max_length=400, null=True, verbose_name='Текст формы'),
        ),
        migrations.AddField(
            model_name='successformstatic',
            name='title_ru',
            field=models.CharField(max_length=128, null=True, verbose_name='Заголовок формы'),
        ),
        migrations.AddField(
            model_name='successformstatic',
            name='title_ua',
            field=models.CharField(max_length=128, null=True, verbose_name='Заголовок формы'),
        ),
    ]
