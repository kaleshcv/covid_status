# Generated by Django 3.0.5 on 2020-05-10 20:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('covidstatus', '0039_auto_20200510_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_date',
            field=models.TextField(default=datetime.datetime(2020, 5, 10, 20, 4, 56, 881609, tzinfo=utc)),
        ),
    ]
