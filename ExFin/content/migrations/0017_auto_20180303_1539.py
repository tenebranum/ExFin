# Generated by Django 2.0.2 on 2018-03-03 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0016_closecredit_closecreditstatic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='closecredit',
            name='image',
            field=models.FileField(upload_to='close_credit', verbose_name='Картинка'),
        ),
    ]