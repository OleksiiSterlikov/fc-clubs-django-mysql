from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Club(models.Model):
    """
    Model for clubs
    """
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    img_emblem = models.ImageField(upload_to='clubs/images/', default='clubs/images/Default_image.png', blank=True)
    since_year = models.IntegerField(null=True)
    description = models.TextField(max_length=256, null=True)
    site_page = models.URLField(max_length=256, null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    approved_by = models.ForeignKey(User, related_name='club_approved_by', null=True, on_delete=models.SET_NULL)
    approved = models.BooleanField(default=False)
    display_on_main_page = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} {self.location}'