from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import *
from .models import SignUp
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import SignUp
from django import forms
from django.utils.translation import ugettext_lazy as _

# Register your models here.
# class SignUpAdmin(admin.ModelAdmin):
# class Meta:
#         model = SignUp
#
# admin.site.register(SignUp,SignUpAdmin)

'''class SignUpUserAdmin(UserAdmin):
    # The forms to add and change user instances

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference the removed 'username' field
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_admin', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('email', 'first_name', 'last_name', 'is_admin')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

admin.site.register(SignUp, SignUpUserAdmin)
'''