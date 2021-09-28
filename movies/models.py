from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    duration = models.CharField(max_length=4)
    premiere = models.CharField(max_length=10)
    classification = models.IntegerField()
    synopsis = models.TextField()

class Genre(models.Model):
    name = models.CharField(max_length=255)
    movie = models.ManyToManyField(Movie, related_name='genres')

