from django.contrib import admin
from .models import Subreddit, Sentiment

# Register your models here.
admin.site.register(Subreddit)
admin.site.register(Sentiment)