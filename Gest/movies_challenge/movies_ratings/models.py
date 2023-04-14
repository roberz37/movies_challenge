from django.db import models

# Create your models here.

class MovieRating(models.Model):
    year = models.IntegerField(null= False)
    vote_average = models.FloatField(null= False)
    quantity = models.IntegerField()

    def __str__(self):
        return f'year: {self.year}, vote average: {self.vote_average}, quantity: {self.quantity}'