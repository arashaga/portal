__author__ = 'arashaga'

from .models import RFCDocument
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import views

class RFCForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super(RFCForm,self).__init__(*args,**kwargs)
        self.helper = FormHelper(self)
        self.helper.field_class = 'form-horizontal'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = '../confirmed/'
        self.helper.add_input(Submit('submit', 'Submit'))



    class Meta:
        model = RFCDocument



