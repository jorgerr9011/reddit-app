from django.db import models

class AnalyzedComment(models.Model):
    author = models.CharField(max_length=255)
    comment = models.TextField()
    sentiment = models.FloatField()

    def __str__(self):
        return self.comment
