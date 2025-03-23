from django.db import models

# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    url = models.URLField()