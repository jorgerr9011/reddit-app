from django.test import TestCase, RequestFactory
from subreddit.views import getSubreddit
from subreddit.models import Subreddit

# Create your tests here.

class ViewsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_get_subreddit(self):
        name = 'java'
        getSubreddit(name)
        subr = Subreddit.objects.all()

        for sub in subr:
            self.assertEqual(sub.subreddit, name)

        subr.delete()

    
    def test_get_subreddit_with_invalid_name(self):
        name = 'error_name'
        self.assertRaises(KeyError, getSubreddit, name)

        
        