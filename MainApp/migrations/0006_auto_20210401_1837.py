# Generated by Django 3.1 on 2021-04-01 18:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MainApp', '0005_auto_20210319_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarif',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarif', models.IntegerField()),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2021, 4, 1, 18, 37, 13, 462499))),
                ('comment', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 1, 18, 37, 13, 461243)),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 1, 18, 37, 13, 460660)),
        ),
        migrations.CreateModel(
            name='Elektro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('el_acc', models.IntegerField()),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2021, 4, 1, 18, 37, 13, 462169))),
                ('comment', models.CharField(max_length=500)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('comment', models.CharField(max_length=500)),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2021, 4, 1, 18, 37, 13, 461667))),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]