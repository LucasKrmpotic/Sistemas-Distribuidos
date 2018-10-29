#!/usr/bin/env python3
import cgi
import csv

form = cgi.FieldStorage()

print("Content-type: text/html\n\n")
print("<html><head><title>CGI</title></head>")
print("<body>")
print("<table>")
print("<tr>")
print("<td>nombre</td><td>legajo</td><td>sexo</td><td>edad</td>")
print("</tr>")
print("<tr>")
print("<td>1</td><td>2</td><td>3</td><td>4</td>")
print("</tr>")
print("</table>")
print("</body>")
print("</html>")