from django.db import models
from django.contrib.auth.models import User
from clubs.models import Club


# Create your models here.
class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    club = models.ManyToManyField(Club)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    approved_by = models.ForeignKey(User, related_name='approved_by', null=True, on_delete=models.SET_NULL)
    approved = models.BooleanField(default=False)
