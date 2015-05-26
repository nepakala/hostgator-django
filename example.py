#!/usr/bin/python
print "Content-type: text/html\n\n";
print "<html><head>";
print "<title>CGI Test</title>";
# import os
# if not os.environ['mod_wsgi.process_group']:
#     print('EMBEDDED MODE')
# else:
#     print('DAEMON MODE')
print "</head><body>";
print "<p>Test page using Python</p>";
print "</body></html>";
