from django.db import models
from datetime import datetime

# Create your models here.
class Leader_Board(models.Model):
    leaderboard_name = models.CharField(max_length=200)

    def __str__(self):
        return self.leaderboard_name
    

class Player(models.Model):
    name = models.CharField(max_length=500)
    guesses = models.IntegerField(null=True, default=0)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
    
    
class Random_Letter(models.Model):
    letter = models.CharField(max_length=1, blank=True)

    def __str__(self):
        return self.letter
