__author__ = 'arashaga'

from tastypie.resources import ModelResource
from .models import RFCDocument
from signup.models import SignUp

class RFCResource(ModelResource):
    class Meta:
        queryset = SignUp.objects.all()
        resource_name = 'rfc'