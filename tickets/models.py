from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tickets(models.Model):
    class Meta():
        db_table = "ticket"
    tickets_from = models.CharField(max_length = 200)
    tickets_to = models.CharField(max_length = 200)
    tickets_datetime = models.TimeField()
    tickets_date = models.DateField()
    tickets_class = models.IntegerField()
    tickets_places = models.IntegerField()
    tickets_user = models.ForeignKey(User, null = True ,blank=True)
    tickets_price = models.IntegerField()
    tickets_paid = models.BooleanField()
