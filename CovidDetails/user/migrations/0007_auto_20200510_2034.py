# Generated by Django 3.0.5 on 2020-05-10 20:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20200510_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postnew',
            name='post_date',
            field=models.DateField(default=datetime.datetime),
        ),
    ]
