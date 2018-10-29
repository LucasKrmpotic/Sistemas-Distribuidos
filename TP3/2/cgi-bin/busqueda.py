#!/usr/bin/env python3
import cgi
import csv

form = cgi.FieldStorage()

print("Content-type: text/html\n\n")
print("<html><head><title>CGI</title></head>")
print("<body>")
print("<table>")
print("<tr><th>nombre</th><th>legajo</th><th>sexo</th><th>edad</th></tr>")
print("<tr><td>1</td><td>2</td><td>3</td><td>4</td></tr>")
print("</table>")
print("</body>")
print("</html>")