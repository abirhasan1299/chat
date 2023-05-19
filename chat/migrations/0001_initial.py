# Generated by Django 4.2.1 on 2023-05-19 05:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=200)),
                ('time', models.DateTimeField(verbose_name=datetime.datetime(2023, 5, 19, 11, 0, 14, 679018))),
            ],
        ),
    ]
