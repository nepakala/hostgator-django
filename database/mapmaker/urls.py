from django.conf.urls import include, url

from mapmaker.views import *

urlpatterns = [
    # url(r'^.*$', addLocation.as_view(), name='mapmaker'),
    url(r'^code/$', showCode.as_view(), name='code'),
    url(r'^preview/$', previewMap.as_view(), name='preview'),
]
