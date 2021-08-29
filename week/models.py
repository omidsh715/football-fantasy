from django.db import models
from django.utils import timezone
# Create your models here.


class CurrentWeekManager(models.Manager):
    def get_queryset(self):
        weeks = super().get_queryset().all()
        for week_start in weeks:
            if timezone.now() < week_start.start_day:
                return week_start


class Week(models.Model):
    choices = [(i, str(i)) for i in range(1, 39)]
    week_number = models.PositiveIntegerField(choices=choices)
    start_day = models.DateTimeField()
    objects = models.Manager()
    current_week = CurrentWeekManager()

    def __str__(self):
        return f'{self.week_number}'

