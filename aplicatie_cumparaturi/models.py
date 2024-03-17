from django.db import models

# Create your models here.

class Produs(models.Model):
    nume = models.CharField(max_length=255, null = False, unique=True)
    cumparat = models.BooleanField(default=False)
