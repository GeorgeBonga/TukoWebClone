from django.db import models
import datetime
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    date_recorded = models.DateField(default=datetime.datetime.utcnow)

