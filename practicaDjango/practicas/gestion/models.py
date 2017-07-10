# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Equipo(models.Model):
    name = models.CharField(primary_key=True, max_length=25)
    foundation = models.IntegerField()
    city = models.CharField(max_length=25)
    stadium = models.CharField(max_length=25)
    coach = models.CharField(max_length=25)
    capacity = models.IntegerField()

    def storage(self):
        self.save()

    def __unicode__(self):
        return self.name

class Jugador(models.Model):
    team = models.ForeignKey('Equipo')
    playerName = models.CharField(max_length=25)
    nacionality = models.CharField(max_length=3)
    age = models.IntegerField()
    heigh = models.IntegerField()
    position = models.CharField(max_length=3)

    def storage():
        self.save()

    def __unicode__(self):
        return self.playerName
