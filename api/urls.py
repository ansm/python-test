from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from education_mgmt import settings
from api.views import *
from rest_framework.authtoken import views as tokenView

urlpatterns = patterns('',
    url(r'^login/', tokenView.obtain_auth_token),
    url(r'^register/$', user_Register, name='user_Register'),
    url(r'^universities/list/$', universities_list, name='universities_list'),
    url(r'^universities/list1/$', universities_list1, name='universities_list1'),
    url(r'^School/add/$', school_create, name='school_create'),
    url(r'^School/list/$', school_list, name='school_list'),
    url(r'^School/details/$', school_details, name='school_details'),
    url(r'^School/update/(?P<pk>[0-9]+)/$', school_update, name='school_update'),
    url(r'^School/delete/(?P<pk>[0-9]+)/$', school_delete, name='school_update'),
    url(r'^Student/add/$', student_add, name='student_add'),
    url(r'^Student/list/$', student_list, name='student_list'),

    
   
    # url(r'^School/delete/$', school_delete, name='school_delete'),
    
)
