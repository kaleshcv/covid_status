# Generated by Django 3.0.5 on 2020-05-12 18:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_auto_20200512_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postnew',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 12, 18, 25, 0, 625560)),
        ),
    ]
