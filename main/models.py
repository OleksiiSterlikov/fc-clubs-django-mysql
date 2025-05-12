from django.db import models

# Create your models here.
class MenuItem(models.Model):
    """
    Model menu items.
    """
    name = models.CharField(max_length=100, null=False)
    url = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name