# Generated by Django 2.1 on 2019-01-03 08:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('TransportationManagement', '0002_auto_20190103_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposer',
            name='Date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
