from django.test import TestCase

from test_whoosh_app.models import Post

class SimpleTest(TestCase):
    def setUp(self):
        Post.objects.create(
            title='first post',
            body='This is my very first post ever in the world!'
        )
        Post.objects.create(
            title='second post',
            body='This is now the second post that I have indexed!'
        )
        Post.objects.create(
            title='third post',
            body='Whoah'
        )
    
    def test_query(self):
        self.assertEqual(
            unicode(Post.objects.query('first')),
            unicode(Post.objects.filter(title='first post'))
        )
        self.assertEqual(
            map(unicode, Post.objects.query('post')),
            map(unicode, Post.objects.all())
        )