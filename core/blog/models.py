import datetime
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    body = models.TextField(verbose_name='Description')
    date_posted = models.DateTimeField(default=datetime.datetime.now, verbose_name='Date Posted')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'