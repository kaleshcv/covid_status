# Generated by Django 3.0.5 on 2020-05-10 20:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20200510_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postnew',
            name='post_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 10, 20, 42, 11, 413538)),
        ),
    ]