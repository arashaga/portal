__author__ = 'arashaga'

from django.conf.urls import  patterns, url
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = patterns('rfc.views',
                       url(r'^api/','rfc_list',name='rfc_list'),
                       url(r'^list/', 'rfc_log_view', name='rfc_log'),
                       url(r'^create/', 'add_rfc', name='rfc_create'),
                       url(r'^confirmed/', 'rfc_creation_confirmation', name='rfc_confirmed'),
                       )