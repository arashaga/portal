from django.db import models
from signup.models import SignUp
from django.contrib.contenttypes.models import ContentType
# Create your models here.


class ObjectPermission(models.Model):
    user = models.ForeignKey(SignUp)
    can_view = models.BooleanField()
    can_change = models.BooleanField()
    can_delete = models.BooleanField()

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()


