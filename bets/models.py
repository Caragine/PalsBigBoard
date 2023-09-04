from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.
User = get_user_model()

class Bet(models.Model):
    bettor1 = models.ForeignKey(User, related_name='bettor1', on_delete=models.CASCADE)
    bettor2 = models.ForeignKey(User, related_name='bettor2', on_delete=models.CASCADE)
    bet_description = models.TextField()
    bettor1risk = models.PositiveIntegerField(verbose_name="My Wager")
    bettor2risk = models.PositiveIntegerField(verbose_name="Opponent's Wager")
    create_date = models.DateTimeField(auto_now_add=True)
    settled = models.BooleanField(default=False)
    settled_date = models.DateTimeField(auto_now=True)
    winner = models.ForeignKey(User, related_name='winner', on_delete=models.CASCADE, blank=True, null=True)
    loser = models.ForeignKey(User, related_name='loser', on_delete=models.CASCADE, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('bets:for_user', kwargs={'username': self.bettor1.username})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.bettor1) + " vs " + str(self.bettor2) + ": " + self.bet_description + " --- " + str(self.bettor1risk) + " to win " + str(self.bettor2risk)
