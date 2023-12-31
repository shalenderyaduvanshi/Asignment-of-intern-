# Generated by Django 4.2.2 on 2023-06-22 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='data',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='data',
            name='weight',
            field=models.FloatField(),
        ),
    ]
