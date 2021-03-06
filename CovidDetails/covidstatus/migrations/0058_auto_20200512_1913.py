# Generated by Django 3.0.5 on 2020-05-12 19:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('covidstatus', '0057_auto_20200512_1825'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='static/gallery')),
                ('img_name', models.TextField(max_length=100)),
                ('img_date', models.DateTimeField(default=datetime.datetime(2020, 5, 12, 19, 13, 42, 124707))),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_date',
            field=models.TextField(default=datetime.datetime(2020, 5, 12, 19, 13, 42, 123859, tzinfo=utc)),
        ),
    ]
