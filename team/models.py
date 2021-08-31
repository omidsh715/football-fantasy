from django.db import models
from django.conf import settings
from week.models import Week
# Create your models here.


class TeamModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    team = models.JSONField()

    def __str__(self):
        return f'{self.user} {self.week}'
