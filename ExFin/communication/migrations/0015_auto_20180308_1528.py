# Generated by Django 2.0.2 on 2018-03-08 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0014_auto_20180308_1524'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faqitem',
            options={'verbose_name': 'Вопрос', 'verbose_name_plural': 'FAQ вопросы'},
        ),
    ]