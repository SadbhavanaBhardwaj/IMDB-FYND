from django.db import models
from users.models import ImdbUser

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Movie(models.Model):
    popularity = models.FloatField()
    director = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    genre = models.ManyToManyField(Genre)

    def save(self, *args, **kwargs):
        self.popularity = round(self.popularity, 1)
        super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Rating(models.Model):
    user = models.ForeignKey(ImdbUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    score = models.IntegerField()



    def __str__(self):
        return str(self.score)
