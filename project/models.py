from django.db import models
from django.utils.encoding import smart_unicode
from company.models import Companies
from state.models import States
from signup.models import SignUp

# Create your models here.

class Projects(models.Model):
    project_name = models.CharField(max_length=120,blank=False)
    project_title = models.CharField(max_length=120,blank=False)
    project_number = models.IntegerField(blank=False,null=True)
    project_address = models.CharField(max_length=120,null=True,blank=True)
    project_city = models.CharField(max_length=120,null=True,blank=True)
    project_state = models.ForeignKey(States)
    project_start = models.DateField()
    project_finish = models.DateField()
    project_owner = models.ForeignKey(Companies)
    Project_creation_date = models.DateTimeField(auto_now_add=True)
    project_active = models.BooleanField()

    def __unicode__(self):
        return smart_unicode(self.project_name)


class ProjectGroup(models.Model):
    project_group_description = models.CharField(max_length=200, null=False)
    project_group_abrv = models.CharField(max_length=20, null=False)
    project_group_timestamp = models.DateTimeField(auto_now_add=True);

    def __unicode__(self):
        return smart_unicode(self.project_group_abrv)

class ProjectContactTitles(models.Model):
    project_contact_title = models.CharField(max_length=10,null=False)
    project_contact_title_description = models.CharField(max_length=120, null=False)

    def __unicode__(self):
        return smart_unicode(self.project_contact_title)


class ProjectContacts(models.Model):
    project_contact = models.ForeignKey(SignUp)
    project_contact_group = models.ForeignKey(ProjectGroup)
    project_contact_title = models.ForeignKey(ProjectContactTitles)
    project_contact_add_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.project_contact)







