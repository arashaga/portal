from django.db import models
from django.utils.encoding import smart_unicode
from state.models import States



# Create your models here.
class Addresses(models.Model):
    address = models.CharField(max_length=120, null=True, blank=True)
    city = models.CharField(max_length=120, null=True, blank=True)
    state = models.ForeignKey(States)
    zipcode = models.CharField(max_length=5)
    phone = models.CharField(max_length=120, null=True, blank=True)
    fax = models.CharField(max_length=120, null=True, blank=True)
    website = models.URLField()
    date_modified = models.DateField(auto_now=True)

    def get_full_address(self):
        list = [self.address, self.city, States.state_abv, self.zipcode]
        return list

    def __unicode__(self):
        address = self.address
        # + '\n'+ self.city + ', '+ self.state
        # + ' '+ self.zipcode

        return smart_unicode(address)
