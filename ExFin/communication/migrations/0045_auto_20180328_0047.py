# Generated by Django 2.0.2 on 2018-03-27 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0044_auto_20180328_0042'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userquestion',
            options={'ordering': ['-updated_at'], 'verbose_name': 'Вопрос пользователя', 'verbose_name_plural': 'Вопросы пользователей'},
        ),
    ]