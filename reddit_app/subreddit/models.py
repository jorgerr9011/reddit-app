from django.db import models

# Create your models here.
class Subreddit(models.Model):
    subreddit = models.CharField(max_length=200)
    title = models.TextField()
    selftext = models.TextField()
    upvote_ratio = models.CharField(max_length=200)
    ups = models.CharField(max_length=200)
    downs = models.CharField(max_length=200, null=True)
    score = models.CharField(max_length=200)
    sent = models.CharField(max_length=200, null=True)
    contObj = models.CharField(max_length=200, null=True)
    contSubj = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.subreddit
        
class Sentiment(models.Model):
    sentiment = models.CharField(max_length=200)
    subreddit = models.CharField(max_length=200, null=True)
    #contObj = models.CharField(max_length=200, null=True)
    #contSubj = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.sentiment