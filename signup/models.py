from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.conf import settings
from django.utils.encoding import smart_unicode
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from address.models import Addresses
#import re

# Create your models here.

#New UserManager
# from objperm.models import ObjectPermission

'''
This is a fully operational user model for Django with a builtin objection permission capability
You need to add the following in the settings

add the signup to the installed apps
AUTH_USER_MODEL = 'signup.SignUp'
ANONYMOUS_USER_ID = -1
 also for testing  you can add below in django 1.6 perhaps
import sys
if 'test' in sys.argv:
    SOUTH_TESTS_MIGRATE = False


'''


class SignUpUserManager(BaseUserManager):
    def create_user(self, email, is_admin, password=None):
        if not email:
            raise ValueError('User must have an email address!')

        user = self.model(
            email=self.normalize_email(email),
            is_admin=False,
            is_active=True,
            # is_superuser = False,
            last_login=timezone.now(),
            date_joined=timezone.now()
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password):
        user = self.create_user(email, True, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


# This class is defined to overcome the issue with the inline form in the admin based on
#http://stackoverflow.com/questions/20889806/use-onetoonefield-inlined-in-django-admin
class AbstractSignUp(models.Model):
    first_name = models.CharField(max_length=120,null=True,blank=True)
    last_name = models.CharField(max_length=120,null=True,blank=True)
    address = models.OneToOneField(Addresses, blank=True, null=True)
    email = models.EmailField(max_length=254,unique=True,db_index=True)
    #active = models.BooleanField()
    #timestamp = models.DateField(auto_now_add=True,auto_now=False)
    date_joined = models.DateField(auto_now_add=True,auto_now=False)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    class Meta:
        abstract = True


# class SignUp(models.Model): with permissions
class SignUp(AbstractSignUp, AbstractBaseUser, PermissionsMixin):
    #class SignUp(AbstractSignUp, AbstractBaseUser):
    objects = SignUpUserManager()

    # delete if backend doesn't work
    supports_object_permissions = True
    supports_anonymous_user = True

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def get_full_name(self):
        # The user is identified by their email address
        return smart_unicode(self.first_name + ' ' + self.last_name)

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    #DO NOT OVERRIDE THIS
    def has_perm(self,perm,obj=None):
        user_obj = self
        if not self.is_authenticated():
            user_obj = self.objects.get(pk=settings.ANONYMOUS_USER_ID)

        if obj is None:
            return False

        ct = ContentType.objects.get_for_model(obj)

        try:
            perm = perm.split('.')[-1].split('_')[0]
        except IndexError:
            return False

        p = ObjectPermission.objects.filter(content_type=ct,
                                            object_id=obj.id,
                                            user=user_obj)
        return p.filter(**{'can_%s' % perm: True}).exists()

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def __unicode__(self):
        return smart_unicode(self.email)


class ObjectPermission(models.Model):
    user = models.ForeignKey(SignUp, related_name='objperm_signup')
    can_view = models.BooleanField()
    can_change = models.BooleanField()
    can_delete = models.BooleanField()

    content_type = models.ForeignKey(ContentType, related_name='objperm_ct')
    object_id = models.PositiveIntegerField()
