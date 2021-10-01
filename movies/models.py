from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=255)
    duration = models.CharField(max_length=5)
    premiere = models.CharField(max_length=10)
    classification = models.IntegerField()
    synopsis = models.TextField()

class Genre(models.Model):
    name = models.CharField(max_length=255)
    movie = models.ManyToManyField(Movie, related_name='genres')

class Review(models.Model):
    stars = models.IntegerField()
    review = models.TextField()
    spoilers = models.BooleanField()
    critic = models.ForeignKey(User, on_delete=models.CASCADE, related_name='critic_reviews', null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews', null=True)

