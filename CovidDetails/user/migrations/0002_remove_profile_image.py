# Generated by Django 3.0.5 on 2020-05-10 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
    ]
