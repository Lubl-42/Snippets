# Generated by Django 3.1 on 2021-03-11 14:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 11, 14, 26, 15, 692152)),
        ),
    ]
