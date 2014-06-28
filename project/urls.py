__author__ = 'arashaga'

from django.conf.urls import patterns, url

from project import views

urlpatterns = patterns('',
    url(r'^$', 'project.views.home', name='index')
)