from django.db import models


# Create your models here.
class Club(models.Model):
    club_name = models.CharField(max_length=64)

    def __str__(self):
        return self.club_name


class Player(models.Model):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)

    pos_choice = (('GK', 'GK'), ('DEF', 'DEF'), ('MID', 'MID'), ('FW', 'FW'))
    position = models.CharField(choices=pos_choice, max_length=3)

    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    price = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

