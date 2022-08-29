# Generated by Django 4.1 on 2022-08-29 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('account_id', models.IntegerField(primary_key=True, serialize=False)),
                ('balance', models.IntegerField(null=True)),
                ('alias', models.CharField(max_length=50, null=True)),
                ('customer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
            ],
            options={
                'verbose_name': 'Cuenta',
                'verbose_name_plural': 'Cuentas',
            },
        ),
    ]
