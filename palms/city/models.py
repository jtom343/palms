from django.db import models

# Create your models here.

#model to store the Exchange rate everyday
class DBRate(models.Model):
    EXdate = models.DateTimeField()
    EXrate = models.IntegerField()
