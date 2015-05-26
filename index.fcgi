#!/home4/newbreed/public_html/tools/custom-maps/pyenv/bin/python
import os
import sys

from flup.server.fcgi import WSGIServer
from django.core.wsgi import get_wsgi_application

sys.path.insert(0, "/home4/newbreed/public_html/tools/custom-maps/database")
os.environ['DJANGO_SETTINGS_MODULE'] = "database.settings"

WSGIServer(get_wsgi_application()).run()