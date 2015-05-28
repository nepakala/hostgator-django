from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from django.views.generic import View
from django.core.context_processors import csrf
from django.template import Context
# from mysite.settings import STATIC_ROOT

# proper logging (not using "print")
# import logging
# logger = logging.getLogger(__name__)

# from hedonometer.models import NYT,Timeseries,Word

# from django.views.decorators.csrf import csrf_exempt, csrf_protect
# from django.core import serializers

# import csv
# import subprocess
# import codecs
# import json
# import datetime

from findcoords import *
from mapmaker.models import City,Markup
from django.contrib.auth.models import User

class showCode(View):
    def get(self, request, *args, **kwargs):
        locations = City.objects.filter(client=request.user)
        markup = Markup.objects.filter(client=request.user)[0]
        rawsvg,rawsvgnocoords = readmaps("/home4/newbreed/public_html/tools/database/mapmaker/mapdata/rawsvgmaplatlon","/home4/newbreed/public_html/tools/database/mapmaker/mapdata/rawsvgmap")
        newmapstring,newhtmlstring = makeMaps(locations,rawsvg,rawsvgnocoords)
        return render(request, 'mapmaker/mapresponse.html', Context({"newmapstring": newmapstring, "newhtmlstring": newhtmlstring, 'markup': markup}))

class previewMap(View):
    def get(self, request, *args, **kwargs):
        locations = City.objects.filter(client=request.user)
        markup = Markup.objects.filter(client=request.user)[0]
        rawsvg,rawsvgnocoords = readmaps("/home4/newbreed/public_html/tools/database/mapmaker/mapdata/rawsvgmaplatlon","/home4/newbreed/public_html/tools/database/mapmaker/mapdata/rawsvgmap")
        newmapstring,newhtmlstring = makeMaps(locations,rawsvg,rawsvgnocoords)
        return render(request, 'mapmaker/mapview.html', Context({"newmapstring": newmapstring, "newhtmlstring": newhtmlstring, 'markup': markup}))

class mapApi(View):
    def get(self, request, username, *args, **kwargs):
        user = User.objects.filter(username=username)[0]
        locations = City.objects.filter(client=user)
        markup = Markup.objects.filter(client=user)[0]
        rawsvg,rawsvgnocoords = readmaps("/home4/newbreed/public_html/tools/database/mapmaker/mapdata/rawsvgmaplatlon","/home4/newbreed/public_html/tools/database/mapmaker/mapdata/rawsvgmap")
        newmapstring,newhtmlstring = makeMaps(locations,rawsvg,rawsvgnocoords)
        return render(request, 'mapmaker/api.html', Context({"newmapstring": newmapstring, "newhtmlstring": newhtmlstring, 'markup': markup}))
