from django.conf.urls import patterns, include, url
from submit import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^login', views.login_form),
	url(r'^submitlogin$', views.submitlogin),
	url(r'^profile$', views.profile),
	url(r'^register$', views.register),
    # Examples:
    # url(r'^$', 'formsusersdemo.views.home', name='home'),
    # url(r'^formsusersdemo/', include('formsusersdemo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
