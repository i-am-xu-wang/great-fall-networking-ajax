# Generated by Django 3.2.9 on 2021-11-02 16:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.CharField(default='11:00 AM', max_length=30),
        ),
    ]