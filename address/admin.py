from django.contrib import admin
from .models import Addresses
from signup.models import SignUp

# Register your models here.

# TODO you need to put the OneToOne field in the Addresses model to get the inline form in the SignupAdmin

def DisplayListInfo(obj):
    return ("%s %s" % (obj.address, obj.city)).upper()


class InlineAddressAdmin(admin.TabularInline):
    model = SignUp


class SignUpAdmin(admin.ModelAdmin):
    inlines = [
        InlineAddressAdmin,
    ]
    list_display = (DisplayListInfo,)


admin.site.register(Addresses, SignUpAdmin)