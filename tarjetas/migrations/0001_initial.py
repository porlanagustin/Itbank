# Generated by Django 4.1 on 2022-08-30 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0002_cuenta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('numero', models.IntegerField()),
                ('cvv', models.IntegerField()),
                ('vto', models.DateTimeField()),
                ('tipo', models.TextField(max_length=20)),
                ('customer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
            ],
            options={
                'verbose_name': 'Tarjeta',
                'verbose_name_plural': 'Tarjetas',
            },
        ),
    ]
