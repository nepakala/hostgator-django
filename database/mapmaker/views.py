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
# from json import dumps
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
        return render(request, "mapmaker/mapresponse.html", Context({"newmapstring": newmapstring, "newhtmlstring": newhtmlstring, "markup": markup}))

class previewMap(View):
    def get(self, request, *args, **kwargs):
        locations = City.objects.filter(client=request.user)
        markup = Markup.objects.filter(client=request.user,version=1)[0]
        rawsvg,rawsvgnocoords = readmaps("/home4/newbreed/public_html/tools/database/mapmaker/mapdata/rawsvgmaplatlon","/home4/newbreed/public_html/tools/database/mapmaker/mapdata/rawsvgmap")
        newmapstring,newhtmlstring = makeMaps(locations,rawsvg,rawsvgnocoords)
        return render(request, "mapmaker/mapview.html", Context({"newmapstring": newmapstring, "newhtmlstring": newhtmlstring, "markup": markup}))

class mapApi(View):
    def get(self, request, username, *args, **kwargs):
        user = User.objects.filter(username=username)[0]
        locations = City.objects.filter(client=user)
        markup = Markup.objects.filter(client=user,version=1)[0]
        rawsvg,rawsvgnocoords = readmaps("/home4/newbreed/public_html/tools/database/mapmaker/mapdata/rawsvgmaplatlon","/home4/newbreed/public_html/tools/database/mapmaker/mapdata/rawsvgmap")
        newmapstring,newhtmlstring = makeMaps(locations,rawsvg,rawsvgnocoords)
        return render(request, "mapmaker/api.html", Context({"newmapstring": newmapstring, "newhtmlstring": newhtmlstring, "markup": markup}))

# import json
# from django.core.serializers.json import DjangoJSONEncoder

def make_html_string(locations):
    boilerplate = """<center><img src="{0}" width="70%"/>
    <h2>{1}<br>{2}<br>{3}</h2></center>
    <p>{4}</p>"""
    
    print('printing out new files')

    newhtmlstring = ''
    for i,location in enumerate(locations):
        newhtmlstring = newhtmlstring + "<div class=\"item white-popup-block mfp-hide\" city=\""+location.location+"\" id=\"location"+str(i)+"\">"
        newhtmlstring = newhtmlstring + boilerplate.format(location.imagelink,location.name,location.company,location.location,location.description)
        newhtmlstring = newhtmlstring + "\n</div>\n"
    return newhtmlstring

class previewMap2(View):
    def get(self, request, *args, **kwargs):
        markup = get_object_or_404(Markup,client=request.user,version=2)
        locations = City.objects.filter(client=request.user)
        # rawsvg,rawsvgnocoords = readmaps("/home4/newbreed/public_html/tools/database/mapmaker/mapdata/rawsvgmaplatlon","/home4/newbreed/public_html/tools/database/mapmaker/mapdata/rawsvgmap")
        # newmapstring,newhtmlstring = makeMaps(locations,rawsvg,rawsvgnocoords)
        html_string =  make_html_string(locations)
        # return render(request, "mapmaker/mapview2.html", Context({"newmapstring": "<div id=\"usmapdiv\"></div>", "newhtmlstring": "", "markup": markup, "locations": json.dumps(locations, cls=DjangoJSONEncoder),}))
        # return render(request, "mapmaker/mapview2.html", Context({"newmapstring": "<div id=\"usmapdiv\"></div>", "newhtmlstring": "", "markup": markup, "locations": locations,}))
        # return render(request, "mapmaker/mapview2.html", Context({"newmapstring": "<div id=\"usmapdiv\"></div>", "newhtmlstring": "", "markup": markup, "locations": [json.dumps(x, cls=DjangoJSONEncoder) for x in locations],}))
        return render(request, "mapmaker/mapview2.html", Context({"newmapstring": "<div id=\"usmapdiv\"></div>", "newhtmlstring": html_string, "markup": markup, "locations": [[x.lon,x.lat] for x in locations],}))

class mapApi2(View):
    def get(self, request, username, *args, **kwargs):
        user = get_object_or_404(User,username=username)
        markup = get_object_or_404(Markup,client=user,version=2)
        locations = City.objects.filter(client=user)
        rawsvg,rawsvgnocoords = readmaps("/home4/newbreed/public_html/tools/database/mapmaker/mapdata/rawsvgmaplatlon","/home4/newbreed/public_html/tools/database/mapmaker/mapdata/rawsvgmap")
        newmapstring,newhtmlstring = makeMaps(locations,rawsvg,rawsvgnocoords)
        return render(request, "mapmaker/api.html", Context({"newmapstring": newmapstring, "newhtmlstring": newhtmlstring, "markup": markup}))

