# Generated by Django 3.1 on 2021-04-24 10:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0008_auto_20210424_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 24, 10, 8, 8, 132377)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 24, 10, 8, 8, 131962)),
        ),
        migrations.AlterField(
            model_name='elektro',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 24, 10, 8, 8, 132708)),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 24, 10, 8, 8, 131528)),
        ),
        migrations.AlterField(
            model_name='tarif',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 24, 10, 8, 8, 133035)),
        ),
    ]
