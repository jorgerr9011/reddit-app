# Generated by Django 4.0 on 2023-05-10 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subreddit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subreddit', models.CharField(max_length=200)),
                ('title', models.TextField()),
                ('selftext', models.TextField()),
                ('upvote_ratio', models.CharField(max_length=200)),
                ('ups', models.CharField(max_length=200)),
                ('downs', models.CharField(max_length=200, null=True)),
                ('score', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sentiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentiment', models.CharField(max_length=200)),
                ('subreddit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='subreddit.subreddit')),
            ],
        ),
    ]