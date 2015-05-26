from django.shortcuts import render
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

def home(request):
    # latest_topic_list = Topic.objects.order_by('-pub_date')[:5]
    # context = {'latest_topic_list': latest_topic_list}
    return render(request, 'database/index.html')

from findcoords import *

class Mapmaker(View):
    def get(self, request, *args, **kwargs):
        # return HttpResponse('Hello, World!')
        return render(request, 'database/mapform.html')

    def post(self, request, *args, **kwargs):
        # return HttpResponse('Thanks for the data. We might sell it.')
        locations = readlocations('/home4/newbreed/public_html/tools/database/database/locations.json')
        # return HttpResponse(json.dumps(locations))
        fillLatLon(locations)
        # writelocations('/home4/newbreed/public_html/tools/database/database/locations.json',locations)
        rawsvg,rawsvgnocoords = readmaps("/home4/newbreed/public_html/tools/database/database/mapdata/rawsvgmaplatlon","/home4/newbreed/public_html/tools/database/database/mapdata/rawsvgmap")
        newmapstring,newhtmlstring = makeMaps(locations,rawsvg,rawsvgnocoords)
        return render(request, 'database/mapresponse.html', Context({"newmapstring": newmapstring, "newhtmlstring": newhtmlstring}))


