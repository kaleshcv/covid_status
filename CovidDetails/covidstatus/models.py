from django.db import models
import django.utils.timezone as dt
import datetime

# Create your models here.

class Destination(models.Model):

    dest_name=models.CharField(max_length=30)
    dest_desc=models.TextField()
    dest_price=models.IntegerField()
    dest_img=models.ImageField(upload_to='static/images')

class Blog(models.Model):

    blog_head=models.CharField(max_length=100)
    blog_para1=models.TextField()
    blog_para2=models.TextField()
    blog_date=models.TextField(default=dt.now())
    blog_author=models.CharField(max_length=30)
    blog_highlight=models.CharField(max_length=100)

class Gallery(models.Model):
    img=models.ImageField(upload_to='static/gallery')
    img_name=models.TextField(max_length=100)
    img_date=models.DateTimeField(default=datetime.datetime.now())


