from django.db import models
#from django.conf import settings
from django.utils.encoding import smart_unicode
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from address.models import Addresses
#import re

# Create your models here.

#New UserManager
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


#class SignUp(models.Model):
class SignUp(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=120,null=True,blank=True)
    last_name = models.CharField(max_length=120,null=True,blank=True)
    address = models.ForeignKey(Addresses,blank=True,null=True)
    email = models.EmailField(max_length=254,unique=True,db_index=True)
    #active = models.BooleanField()
    #timestamp = models.DateField(auto_now_add=True,auto_now=False)
    date_joined = models.DateField(auto_now_add=True,auto_now=False)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = SignUpUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def get_full_name(self):
        # The user is identified by their email address
        return smart_unicode(self.first_name + ' ' + self.last_name)

    def get_short_name(self):
        # The user is identified by their email address
        return self.email


    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def __unicode__(self):
        return smart_unicode(self.email)


