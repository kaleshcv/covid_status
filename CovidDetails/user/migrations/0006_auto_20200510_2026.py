# Generated by Django 3.0.5 on 2020-05-10 20:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200510_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postnew',
            name='post_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 10, 20, 26, 34, 663673, tzinfo=utc)),
        ),
    ]
