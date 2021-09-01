from django.db import models
from week.models import Week
from players.models import Player

# Create your models here.


class PlayerPoint(models.Model):
    """

    for points of a player on specific week

    """
    player = models.ForeignKey(Player, on_delete=models.CASCADE, blank=False)
    week = models.ForeignKey(Week, on_delete=models.CASCADE, blank=False)
    point = models.IntegerField(default=0, blank=False)
    description = models.TextField(blank=True)

    class Meta:
        unique_together = ('player', 'week')
