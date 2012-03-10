from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^mapstraction$', 'django.views.generic.simple.direct_to_template', {'template': 'mapstraction.html'}),
    url(r'^crime$', 'django.views.generic.simple.direct_to_template', {'template': 'crime.html'}),
    url(r'^crime_heatmap$', 'django.views.generic.simple.direct_to_template', {'template': 'crime_heatmap.html'}),
    url(r'^crime.json$', 'maps.crime.views.crime_list'),
    url(r'^sandwich$', 'django.views.generic.simple.direct_to_template', {'template': 'sandwich.html'}),
)
