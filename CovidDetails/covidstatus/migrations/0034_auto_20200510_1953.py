# Generated by Django 3.0.5 on 2020-05-10 19:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('covidstatus', '0033_blog_blog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_date',
            field=models.TextField(default=datetime.datetime(2020, 5, 10, 19, 53, 2, 565507, tzinfo=utc)),
        ),
    ]