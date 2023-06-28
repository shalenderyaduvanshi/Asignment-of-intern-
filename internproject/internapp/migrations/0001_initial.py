# Generated by Django 4.2.2 on 2023-06-22 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DATA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField()),
                ('company', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
                ('item', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(max_length=100)),
                ('weight', models.FloatField(max_length=100)),
                ('request_for_shipment', models.CharField(max_length=100)),
                ('tracking_id', models.CharField(max_length=100)),
                ('shipment_size', models.CharField(max_length=100)),
                ('box_count', models.IntegerField()),
                ('specification', models.CharField(max_length=100)),
                ('checklist_quantity', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'DATA',
            },
        ),
        migrations.CreateModel(
            name='USER',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'USER',
            },
        ),
    ]
