__author__ = 'arashaga'

from rest_framework import serializers
from .models import RFCDocument


class RFCSerializer(serializers.ModelSerializer):
    class Meta:
        model =RFCDocument

