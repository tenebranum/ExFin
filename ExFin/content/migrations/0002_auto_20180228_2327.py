# Generated by Django 2.0.2 on 2018-02-28 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staticpage',
            options={'verbose_name': 'Статическая страница', 'verbose_name_plural': 'Статически страницы'},
        ),
        migrations.AddField(
            model_name='staticpage',
            name='link',
            field=models.CharField(default=1, help_text='Используйте ссылки вида /url', max_length=255, verbose_name='URL-адрес'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='spoiler',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='spoiler_files', verbose_name='Файл'),
        ),
    ]
