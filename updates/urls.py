from django.conf.urls import url
from . import views

from django.conf import settings

urlpatterns = [
    url(r'^$', views.project_list, name='project_list'),
    url(r'^project/(?P<pk>\d+)/$', views.project_detail, name='project_detail'),
    url(r'^subsystem/(?P<pk_sub>\d+)/$', views.subsystem_detail, name='subsystem_detail'),
    #url(r'^project/(?P<pk_proj>\d+)/subsystem/(?P<pk_sub>\d+)/$', views.subsytem_detail, name='subsystem_detail'),
]