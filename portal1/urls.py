from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from rfc.api import RFCResource


rfc_resource = RFCResource()
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    url(r'^$', 'signup.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^members/projects/', include('project.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profile/', 'signup.views.profile', name='profile'),
    #url(r'^members/rfc/', 'rfc.views.rfc_log_view', name='rfc_log'),
    #url(r'^members/rfc/create/', 'rfc.views.add_rfc', name='rfc_create'),
    url(r'^members/', 'signup.views.members', name='members'),
    url(r'^members/rfc/', include('rfc.urls')),
    #url(r'^api/', 'rfc.views.rfc_log_json', name='rfc_json'),
   #(r'^api/', rfc_log_json().as_view),
   url(r'^login/$', 'signup.views.user_login', name='login'),
   url(r'^logout/$', 'signup.views.user_logout', name='logout'),

   #url(r'^api/','rfc_list',name='rfc_list'),
)

if settings.DEBUG:
    urlpatterns +=  static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns +=  static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)