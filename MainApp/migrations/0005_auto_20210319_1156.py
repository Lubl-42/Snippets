# Generated by Django 3.1 on 2021-03-19 11:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_auto_20210318_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 19, 11, 56, 6, 942202)),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 19, 11, 56, 6, 941673)),
        ),
    ]