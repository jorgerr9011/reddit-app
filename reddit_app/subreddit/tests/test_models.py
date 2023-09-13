from django.test import TestCase
from subreddit.models import Subreddit, Sentiment

# Create your tests here.
class SubredditModelTest(TestCase):
    def test_create_subreddit(self):
        subreddit = Subreddit.objects.create(
            subreddit='test_subreddit',
            title='Test Title',
            selftext='Test Selftext',
            upvote_ratio='0.75',
            ups='100',
            downs='10',
            score='90'
        )
        self.assertEqual(subreddit.subreddit, 'test_subreddit')
        self.assertEqual(subreddit.title, 'Test Title')
        self.assertEqual(subreddit.selftext, 'Test Selftext')
        self.assertEqual(subreddit.upvote_ratio, '0.75')
        self.assertEqual(subreddit.ups, '100')
        self.assertEqual(subreddit.downs, '10')
        self.assertEqual(subreddit.score, '90')

    def test_subreddit_str(self):
        subreddit = Subreddit.objects.create(
            subreddit='test_subreddit',
            title='Test Title',
            selftext='Test Selftext',
            upvote_ratio='0.75',
            ups='100',
            downs='10',
            score='90'
        )
        self.assertEqual(str(subreddit), 'test_subreddit')

class SentimentModelTest(TestCase):
    def test_create_sentiment(self):
        subreddit = Subreddit.objects.create(
            subreddit='test_subreddit',
            title='Test Title',
            selftext='Test Selftext',
            upvote_ratio='0.75',
            ups='100',
            downs='10',
            score='90'
        )
        sentiment = Sentiment.objects.create(
            sentiment='positive',
            subreddit=subreddit
        )
        self.assertEqual(sentiment.sentiment, 'positive')
        self.assertEqual(sentiment.subreddit, subreddit)

    def test_sentiment_str(self):
        subreddit = Subreddit.objects.create(
            subreddit='test_subreddit',
            title='Test Title',
            selftext='Test Selftext',
            upvote_ratio='0.75',
            ups='100',
            downs='10',
            score='90'
        )
        sentiment = Sentiment.objects.create(
            sentiment='positive',
            subreddit=subreddit
        )
        self.assertEqual(str(sentiment), 'positive')