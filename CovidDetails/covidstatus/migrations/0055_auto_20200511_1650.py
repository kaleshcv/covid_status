# Generated by Django 3.0.5 on 2020-05-11 16:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('covidstatus', '0054_auto_20200511_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_date',
            field=models.TextField(default=datetime.datetime(2020, 5, 11, 16, 50, 5, 786200, tzinfo=utc)),
        ),
    ]
