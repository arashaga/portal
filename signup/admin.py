from django.contrib.admin import ModelAdmin
from .forms import *

from .models import SignUp
from django import forms
from django.utils.translation import ugettext_lazy as _
from address.models import Addresses
from .reverseadmin import ReverseModelAdmin
# Register your models here.
# class SignUpAdmin(admin.ModelAdmin):
# class Meta:
# model = SignUp
#
# admin.site.register(SignUp,SignUpAdmin)


# class SignUpAdmin(admin.ModelAdmin):
#    inlines = (InlineAddressAdmin,)
#
#    # fieldsets = ((_('Basic Information'),
#    #               {'fields':('first_name','last_name',
#    #               'email','password'),
#    #                }),
#    #               (_('Permissions'),{'fields':('is_active','is_admin')}),
#    # )
#
#    list_display = ('first_name','last_name','email')
#    list_display_links = ('email',)
#    # list_editable = ('address',)
#    list_filter = ('is_admin',)
#    #raw_id_fields = ('address',)
#    #readonly_fields = ('address_report',)
#
# #admin.site.unregister(SignUp)
# admin.site.register(SignUp,SignUpAdmin)
class AddressesForm(admin.TabularInline):
    model = Addresses


# class SignUpAdmin(ReverseModelAdmin):
class SignUpAdmin(ModelAdmin):
    inline_type = 'stacked'
    # inline_reverse = ('address',)
    inlines = (AddressesForm,)

    fields = (
    ('first_name', 'last_name'), 'email', 'password', ('is_active', 'is_admin', 'is_superuser'), 'user_permissions')
    filter_horizontal = ('user_permissions',)


admin.site.register(SignUp, SignUpAdmin)

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