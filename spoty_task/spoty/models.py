from django.db import models
from django.contrib.auth.models import User, auth
import random

# Create your models here.

class song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    release_date = models.DateField()
    ranking = models.FloatField( default=0.0)
    id = models.PositiveIntegerField(default=random.randint(1,10000), primary_key=True)

    def __str__(self):
        return f"{self.title} - {self.artist}"

class reviews(models.Model):
    song = models.ForeignKey(song, on_delete=models.CASCADE)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.user}"