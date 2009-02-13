=======================
django-whoosh
=======================

This is an integration layer that sits between Whoosh and Django so that
full-text searching can be not only possible within any Django project, but
extremely easy as well.

Here's how a django-whoosh enabled model might look:

    import datetime
    from django.db import models
    from django_whoosh.managers import WhooshManager

    class Post(models.Model):
        title = models.CharField(max_length=55)
        body = models.TextField()
        date_posted = models.DateTimeField(default=datetime.datetime.now)
    
        # The first argument is the default query field
        objects = WhooshManager('title', fields=['title', 'body'])
    
        def __unicode__(self):
            return self.title


You just have to add one setting to your settings.py:

    WHOOSH_STORAGE_DIR = '/data/whoosh'


Here's how you would use it:

    >>> p = Post(title='first post', body='This is my first post')
    >>> p.save() # The new model is already added to the index
    >>> Post.objects.query('first')
    [<Post: first post>]