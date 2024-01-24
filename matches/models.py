from django.db import models

from players.models import Player


class Matches(models.Model):
    tournament = models.CharField(max_length=200)
    date = models.DateField()
    match_round = models.CharField(max_length=200)
    duration = models.IntegerField()
    winner = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name='win_matches', blank=True, null=True
    )
    loser = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name='lose_matches', blank=True, null=True
    )
