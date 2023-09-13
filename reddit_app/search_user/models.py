from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100)
    karma_total = models.IntegerField()
    karma_links = models.IntegerField()
    karma_comments = models.IntegerField()
    fecha_creacion = models.DateField()
    subreddit_principal = models.CharField(max_length=1000)
    karma_logros = models.IntegerField()
    snoovatar_img = models.ImageField()
