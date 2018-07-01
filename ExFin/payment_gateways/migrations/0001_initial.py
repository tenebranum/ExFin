# Generated by Django 2.0.2 on 2018-04-05 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tcash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Сумма платежа (sum)')),
                ('note', models.CharField(max_length=128, verbose_name='Примечание (note)')),
                ('type', models.CharField(max_length=32, verbose_name='Тип (in/out, type)')),
                ('pb_code', models.CharField(max_length=128, verbose_name='ID платежа в системе PrivatBank')),
                ('vreme', models.DateTimeField(auto_now_add=True, verbose_name='Дата сохранения')),
            ],
            options={
                'verbose_name_plural': 'Turnes cash (test example of tcash)',
                'verbose_name': 'Turnes cash (test example of tcredits)',
            },
        ),
        migrations.CreateModel(
            name='Tcredits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.PositiveIntegerField(verbose_name='ID клиента (client_id)')),
                ('suma', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Сумма кредита (suma)')),
                ('vnoska', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Платеж (vnoska)')),
                ('egn', models.PositiveIntegerField(verbose_name='ИНН (egn)')),
                ('contract_num', models.PositiveIntegerField(verbose_name='Номер договора (contract_num)')),
            ],
            options={
                'verbose_name_plural': 'Turnes credits (test example of tcredits)',
                'verbose_name': 'Turnes credit (test example of tcredits)',
            },
        ),
        migrations.CreateModel(
            name='Tpersons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Имя клиента (name)')),
                ('name2', models.CharField(max_length=64, verbose_name='Отчество клиента (name2)')),
                ('name3', models.CharField(max_length=64, verbose_name='Фамилия клиента (name3)')),
                ('egn', models.PositiveIntegerField(verbose_name='ИНН (egn)')),
            ],
            options={
                'verbose_name_plural': 'Turnes persons (test example of tpersons)',
                'verbose_name': 'Turnes person (test example of tpersons)',
            },
        ),
    ]