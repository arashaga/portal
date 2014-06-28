from django.db import models
from address.models import Addresses

# Create your models here.
class Companies (models.Model):
    company_name = models.CharField(max_length=120,unique=True,blank=False) #this should be handeled in form
    company_abv = models.CharField(max_length=10,blank=False)
    company_address = models.ForeignKey(Addresses)
    is_public = models.BooleanField()
    date_modified = models.DateField(auto_now=True)

    def __unicode__(self):
        return (self.company_name)
"""TODO: This should be in the form once people insert company name
    def get_company_abv(self):
        s = self
        s = s.title()
        return "".join(e[0] for e in s.split())
"""