# Generated by Django 3.0.5 on 2020-05-11 09:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('covidstatus', '0051_auto_20200511_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_date',
            field=models.TextField(default=datetime.datetime(2020, 5, 11, 9, 51, 57, 274159, tzinfo=utc)),
        ),
    ]