from django.db import models
from django.contrib.auth.models import User
from clubs.models import Club


# Create your models here.
class Player(models.Model):
    """
    Model for players
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    club = models.ForeignKey(Club, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    approved_by = models.ForeignKey(User, related_name='player_approved_by', null=True, on_delete=models.SET_NULL)
    approved = models.BooleanField(default=False)
    display_on_main_page = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
