from django.db import models
from state.models import States


# Create your models here.
class Addresses(models.Model):
    address = models.CharField(max_length=120,null=True,blank=True)
    city = models.CharField(max_length=120,null=True,blank=True)
    state = models.ForeignKey(States)
    phone = models.CharField(max_length=120,null=True,blank=True)
    fax = models.CharField(max_length=120,null=True,blank=True)
    website = models.URLField()
    date_modified = models.DateField(auto_now=True)