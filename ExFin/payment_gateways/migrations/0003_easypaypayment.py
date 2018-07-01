# Generated by Django 2.0.2 on 2018-04-06 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_gateways', '0002_auto_20180405_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='EasypayPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_id', models.IntegerField(verbose_name='Номер EF в системе EasyPay')),
                ('order_id', models.BigIntegerField(verbose_name='Уникальный идентификатор транзакции EasyPay')),
                ('account', models.CharField(max_length=128, verbose_name='Идентификатор пользователя (№ договора)')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Cумма платежа')),
                ('confirmed', models.BooleanField(default=False, verbose_name='Подтвержден?')),
                ('confirmed_dt', models.DateTimeField(blank=True, null=True, verbose_name='Дата заказа')),
                ('canceled', models.BooleanField(default=False, verbose_name='Отменен?')),
                ('cancel_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата отмены заказа')),
            ],
            options={
                'verbose_name_plural': 'Транзакции EasyPay',
                'verbose_name': 'Транзакция EasyPay',
            },
        ),
    ]
