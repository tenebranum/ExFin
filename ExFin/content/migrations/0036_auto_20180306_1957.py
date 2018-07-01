# Generated by Django 2.0.2 on 2018-03-06 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0035_auto_20180306_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpagestatic',
            name='credit_block',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='content.CreditRateStatic', verbose_name='Блок кредитные тарифы'),
        ),
        migrations.RemoveField(
            model_name='mainpagestatic',
            name='credit_close',
        ),
        migrations.AddField(
            model_name='mainpagestatic',
            name='credit_close',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='content.CloseCreditStatic', verbose_name='Блок как закрыть кредит'),
        ),
        migrations.AlterField(
            model_name='mainpagestatic',
            name='departments',
            field=models.ManyToManyField(to='department.Department', verbose_name='Отделения'),
        ),
        migrations.AlterField(
            model_name='mainpagestatic',
            name='discount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='content.DiscountStatic', verbose_name='Блок акция'),
        ),
        migrations.RemoveField(
            model_name='mainpagestatic',
            name='security',
        ),
        migrations.AddField(
            model_name='mainpagestatic',
            name='security',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='content.SecurityStatic', verbose_name='Блок о параметрах защиты'),
        ),
    ]
