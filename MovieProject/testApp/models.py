from django.db import models

# Create your models here.
class MovieInfo(models.Model):
    moviename=models.CharField(max_length=30)
    releasedate=models.DateField()
    actor=models.CharField(max_length=30)
    actress=models.CharField(max_length=30)
    rating=models.FloatField()
