# Generated by Django 3.0.11 on 2020-12-19 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SabjiAtHome', '0004_auto_20201219_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
