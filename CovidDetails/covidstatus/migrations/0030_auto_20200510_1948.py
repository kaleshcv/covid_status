# Generated by Django 3.0.5 on 2020-05-10 19:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('covidstatus', '0029_auto_20200510_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_date',
            field=models.DateField(verbose_name=datetime.datetime(2020, 5, 10, 19, 48, 30, 301299, tzinfo=utc)),
        ),
    ]
