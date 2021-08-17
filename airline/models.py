from django.db import models
from django.utils import timezone

class Flight(models.Model):
    date=models.DateTimeField(default=timezone.now)
    departure=models.CharField(max_length=100)
    arrival=models.CharField(max_length=100)
    price=models.IntegerField()

    def __str__(self):
        return self.departure +"-" + self.arrival
