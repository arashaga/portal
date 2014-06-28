from django.db import models

# Create your models here.
class States(models.Model):
    state_abv = models.CharField(max_length=2,blank=False)
