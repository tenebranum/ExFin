# Generated by Django 2.0.2 on 2018-03-02 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20180301_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuAboutItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название пункта')),
                ('link', models.CharField(help_text='Используйте ссылку вида /#html_id для блока лэндинга. Остальные ссылки указывать полностью (https://...)', max_length=255, verbose_name='URL-адрес')),
            ],
            options={
                'verbose_name_plural': 'Пункты меню на странице "О нас"',
                'verbose_name': 'Пункт меню',
            },
        ),
    ]
