from django.db import models


# Create your models here.
class Tariff(models.Model):
    time = models.IntegerField()
    title = models.TextField()
    subTitle = models.TextField()
