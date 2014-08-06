from django.db import models

# Create your models here.
from django.utils.encoding import smart_unicode


class States(models.Model):
    state_abv = models.CharField(max_length=2, blank=False)

    def __unicode__(self):
        return smart_unicode(self.state_abv)