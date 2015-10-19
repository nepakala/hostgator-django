from django.conf.urls import include, url

from mapmaker.views import *

urlpatterns = [
    # url(r'^.*$', addLocation.as_view(), name='mapmaker'),
    url(r'^code/$', showCode.as_view(), name='code'),
    url(r'^preview/$', previewMap.as_view(), name='preview'),
    url(r'^api/(?P<username>[\w]+)/$', mapApi.as_view(), name='api'),
    url(r'^preview/v2/$', previewMap2.as_view(), name='preview'),
    url(r'^api/v2/(?P<username>[\w]+)/$', mapApi2.as_view(), name='api'),
    
]







