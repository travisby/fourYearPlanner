from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.views.generic import ListView, DetailView
from banner.models import Course, Section
from banner.views import hello, courses_by_major_id, courses_by_minor_id, sections_by_semester, all_courses, track_section

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fourYearPlanner.views.home', name='home'),
    # url(r'^fourYearPlanner/', include('fourYearPlanner.foo.urls')),

    url(r'^hello/$', 'banner.views.hello'),

    url(r'^courses/$', ListView.as_view(model=Course)),
    url(r'^courses/by_major/(\d+)/$', 'banner.views.courses_by_major_id'),
    url(r'^courses/by_minor/(\d+)/$', 'banner.views.courses_by_minor_id'),
    url(r'^courses/Sections_by_semester/(\d+)/$', 'banner.views.sections_by_semester'),
    url(r'^sections/Section/$', ListView.as_view(model=Section,)),
    url(r'^courses/AllCourses/(\d+)/(\d+)/$', 'banner.views.all_courses'),
    url(r'^courses/by_major/\d+/$', 'banner.views.courses_by_major_id'),
    url(r'^courses/by_minor/\d+/$', 'banner.views.courses_by_minor_id'),
    url(r'^courses/Sections_by_semester/\d+/$', 'banner.views.sections_by_semester'),
    url(r'^sections/Section/$', ListView.as_view(model=Section,)),
    url(r'^courses/AllCourses/$', 'banner.views.all_courses'),
    url(r'^sections/register/(?P<section_id>\d+)$', 'banner.views.register_for_class'),
    url(r'^sections/register/$', 'banner.views.schedule'),
    url(r'^sections/track/$', 'banner.views.track_section'),

    # not sure if url is correct here
    url(r'^sections/(?P<pk>\d+)/$', DetailView.as_view(model=Section, template_name='sections/dvSection.html')),


    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)



# ListView, list of objects. while executing, self.object_list will contain list of objects

# DetailView, page representing individual object. while executing, self.object will contain object being
# operated on
