# Generated by Django 3.0.11 on 2020-12-27 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SabjiAtHome', '0011_orderupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default=0, max_length=100),
        ),
    ]
