# coding: utf-8
import cgi
import sys
from io import BytesIO
import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()
print 'Content-Type: text/html\r\n\r\n'
print form
