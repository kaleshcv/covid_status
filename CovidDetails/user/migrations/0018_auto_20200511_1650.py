# Generated by Django 3.0.5 on 2020-05-11 16:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_auto_20200511_1022'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profilenew',
        ),
        migrations.AlterField(
            model_name='postnew',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 11, 16, 50, 5, 786815)),
        ),
    ]
