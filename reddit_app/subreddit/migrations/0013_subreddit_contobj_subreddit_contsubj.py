# Generated by Django 4.0 on 2023-06-08 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subreddit', '0012_subreddit_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='subreddit',
            name='contObj',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subreddit',
            name='contSubj',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
