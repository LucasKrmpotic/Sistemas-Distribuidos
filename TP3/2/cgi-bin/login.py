#!/usr/bin/env python3
from http import cookies
import cgi
import csv

form = cgi.FieldStorage()
leg = form.getvalue('legajo')
psw = form.getvalue('password')

with open('bd.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    logeo = False
    for row in reader:
        if (row['legajo'] == leg):
            if(row['password'] == psw):
                logeo = True
                
    if (logeo): #ver como llamar a modificacion.py

    else: 

print("Content-type: text/html\n\n")
print("<html><head><title>CGI</title></head>")
print("<body>")
print("<font color = blue>\n")
print("<TITLE>CGI script output</TITLE>")
print("<h1 style=\"TEXT-ALIGN: center\">Error en Login :(</h1>\n")
print("</font>\n")
print("</body>")
print("</html>")
