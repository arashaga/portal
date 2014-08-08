__author__ = 'arashaga'

from django.conf.urls import patterns, url

from project import views

urlpatterns = patterns('project.views',
                       url(r'^list/(?P<pk>\d+)', 'project_info', name='project_info'),

)