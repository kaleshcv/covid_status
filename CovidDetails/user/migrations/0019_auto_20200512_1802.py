# Generated by Django 3.0.5 on 2020-05-12 18:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_auto_20200511_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='postnew',
            name='post_image',
            field=models.ImageField(null=True, upload_to='static/post_images'),
        ),
        migrations.AlterField(
            model_name='postnew',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 12, 18, 2, 23, 492027)),
        ),
    ]
