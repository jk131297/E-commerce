# Generated by Django 3.0.11 on 2020-12-24 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SabjiAtHome', '0010_auto_20201223_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=5000)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
