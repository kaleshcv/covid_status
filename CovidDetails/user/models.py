from django.db import models
import datetime

# Create your models here.

class Postnew(models.Model):

    post_title=models.CharField(max_length=100)
    post_content=models.TextField()
    post_image=models.ImageField(null=True,upload_to='static/post_images')
    post_date=models.DateTimeField(default=datetime.datetime.now())
    post_owner=models.CharField(max_length=100)






