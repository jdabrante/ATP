from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=200)
    hand = models.CharField(max_length=1, choices=[('R', 'Rigth'), ('L', 'Left')])
    country = models.CharField(max_length=200)
    birthdate = models.DateField()
