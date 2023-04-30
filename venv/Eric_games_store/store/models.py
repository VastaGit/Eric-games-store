from django.db import models
from djmoney.models.fields import MoneyField

class Game(models.Model):
  name = models.CharField(max_length=100)
  price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
  released_date = models.DateField(null=True)
  rating_score = models.FloatField(null=True)