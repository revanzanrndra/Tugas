from django.db import models

# Create your models here.

class MovieWatchlist(models.Model):
    watched = models.CharField(max_length=225)
    title = models.CharField(max_length=225)
    rating = models.IntegerField()
    release_date = models.CharField(max_length=225)
    review = models.TextField()