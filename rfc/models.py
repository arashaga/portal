from django.db import models
from project.models import Projects, ProjectContacts
from signup.models import SignUp
from django.utils.encoding import smart_unicode
import django_tables2 as tables

# Create your models here.


class RFCDocument(models.Model):

    rfc_number = models.AutoField(primary_key=True)
    rfc_title= models.CharField(max_length=254, null=True, blank = False)
    rfc_project = models.ForeignKey(Projects,unique=False)
    rfc_issued_to = models.ForeignKey(ProjectContacts,related_name='rfc_issued_to',unique=False)
    rfc_drawing_detail_number = models.CharField(max_length=5, null=True, blank = True)
    rfc_specification_section = models.CharField(max_length=20, null=True, blank = True)
    rfc_drawing_page_number = models.CharField(max_length=15, null=True, blank = True)
    rfc_question = models.TextField()
    rfc_issued_by = models.ForeignKey(ProjectContacts,related_name='rfc_issued_by')
    rfc_issued_date = models.DateField(auto_now=True)
    rfc_answer = models.TextField()
    rfc_required_fls_review = models.BooleanField()
    rfc_required_sketch = models.BooleanField()
    rfc_required_fcd = models.BooleanField()
    rfc_answer_reviewed_by = models.ForeignKey(ProjectContacts,related_name='rfc_ans_rev_by',unique=False)
    rfc_answered_date_architect = models.DateField(auto_now=True)
    rfc_answer_authorized_by = models.ForeignKey(ProjectContacts, related_name='rfc_ans_auth_by',unique=False)
    rfc_answer_issued_date = models.DateField(auto_now=True)


    def __unicode__(self):
        return smart_unicode(self.rfc_title)

    def rfc_logger(self):
        L = {
        'rfc_number': smart_unicode(self.rfc_number),
        'rfc_issued_date': smart_unicode(self.rfc_issued_date),
        'rfc_questions' :smart_unicode(self.rfc_question),
        'rfc_answer':smart_unicode(self.rfc_answer),
        'rfc_answer_issued_date': smart_unicode(self.rfc_answer_issued_date),
        'rfc_answer_duration': smart_unicode(self.rfc_answer_issued_date),
            }
        return L

    def rfc_logger2(self):
        L = []
       # L[0] = smart_unicode(self.rfc_number) if self.rfc_number else '1'
        L[0] = '1' if self.rfc_number else smart_unicode(self.rfc_number)
        L[1] = smart_unicode(self.rfc_issued_date) if self.rfc_issued_date else '2/12/01'
        L[2]= smart_unicode(self.rfc_question) if self.rfc_question else 'What?'
        L[3] = smart_unicode(self.rfc_answer) if self.rfc_answer else 'Ha!'
        L[4] = smart_unicode(self.rfc_answer_issued_date) if self.rfc_answer_issued_date else '2/12/01'
        L[5] = smart_unicode(self.rfc_answer_issued_date - self.rfc_issued_date) if self.rfc_answer_issued_date and self.rfc_issued_date else '2/12/01'

        return L

