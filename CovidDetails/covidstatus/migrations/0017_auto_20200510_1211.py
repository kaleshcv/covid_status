# Generated by Django 3.0.5 on 2020-05-10 12:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('covidstatus', '0016_auto_20200510_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_date',
            field=models.DateField(verbose_name=datetime.datetime(2020, 5, 10, 12, 11, 4, 151898, tzinfo=utc)),
        ),
    ]
