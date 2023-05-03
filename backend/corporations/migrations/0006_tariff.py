# Generated by Django 4.1.1 on 2023-04-25 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corporations', '0005_department_staff_designation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('tariff_ID', models.AutoField(primary_key=True, serialize=False)),
                ('tariff_name', models.CharField(max_length=100)),
                ('min_charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('above_charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('min_KL', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
