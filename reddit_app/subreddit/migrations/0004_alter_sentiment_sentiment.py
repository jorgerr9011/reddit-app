# Generated by Django 4.0 on 2023-06-07 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subreddit', '0003_subreddit_sent_alter_sentiment_sentiment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentiment',
            name='sentiment',
            field=models.CharField(default='', max_length=200),
        ),
    ]
