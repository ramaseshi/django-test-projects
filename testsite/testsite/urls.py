from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^page2/$', 'myapp.views.index'),
    # Examples:
    # url(r'^$', 'testsite.views.home', name='home'),
    # url(r'^testsite/', include('testsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
#    url(r'^page1/$', 'myapp.views.text_form'),
    url(r'^tweet/$', 'myapp.views.textform'),
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^form/$', 'myapp.views.textform'),
)
