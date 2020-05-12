# Generated by Django 3.0.5 on 2020-05-11 10:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_auto_20200511_0958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilenew',
            name='image',
        ),
        migrations.AddField(
            model_name='profilenew',
            name='aboutme',
            field=models.CharField(default='Anonym', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='postnew',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 11, 10, 22, 21, 207443)),
        ),
        migrations.AlterField(
            model_name='profilenew',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 11, 10, 22, 21, 206928)),
        ),
    ]