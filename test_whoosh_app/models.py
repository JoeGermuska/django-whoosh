import datetime

from django.db import models

from django_whoosh.managers import WhooshManager

class Post(models.Model):
    title = models.CharField(max_length=55)
    body = models.TextField()
    date_posted = models.DateTimeField(default=datetime.datetime.now)
    
    objects = WhooshManager('title', fields=['title', 'body'])
    
    def __unicode__(self):
        return self.title