from django.db import models

# Create your models here.


class Details(models.Model):
    phone = models.IntegerField()
    provider = models.CharField(max_length=10)
    amount = models.IntegerField()

