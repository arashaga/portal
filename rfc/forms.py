__author__ = 'arashaga'

from .models import RFCDocument
from django.forms import ModelForm, TextInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Div
from project.models import ProjectContacts
import views


# TODO I got to the point that I have to create fieldset and organize everything in equal columns ..read below
# I jumped to work on populaing the RFCnumber and Project info in there
class RFCForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RFCForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.field_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = '../confirmed/'
        # self.helper.layout = Layout(
        # Div(
        #         Fieldset(
        #             '',
        #             'rfc_title',
        #             'rfc_project',
        #             'rfc_issued_to', #NOTICE THE "ID" AT THE END IS REMOVED FROM THE DATABASE FIELD
        #      ),
        #         css_class='col-md-3'
        #     ),
        #     Div(
        #         Fieldset(
        #             '',
        #             'rfc_number',
        #             'rfc_issued_date',
        #             ),
        #         css_class='col-md-3'
        #     ),
        # )
        self.helper.add_input(Submit('submit', 'Submit'))


    class Meta:
        model = RFCDocument
        widgets = {
            'rfc_project': TextInput(attrs={'readonly': 'readonly'}),
            'rfc_issued_to': TextInput(attrs={'readonly': 'readonly'}),
            'rfc_issued_by': TextInput(attrs={'readonly': 'readonly'}),
            'rfc_issued_date': TextInput(attrs={'readonly': 'readonly'}),
            'rfc_answer_reviewed_by': TextInput(attrs={'readonly': 'readonly'}),
            'rfc_answer_authorized_by': TextInput(attrs={'readonly': 'readonly'}),
        }




