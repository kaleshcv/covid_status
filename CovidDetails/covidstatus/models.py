from django.db import models
import django.utils.timezone as dt

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
    blog_date=models.DateField(dt.now())
    blog_author=models.CharField(max_length=30)
