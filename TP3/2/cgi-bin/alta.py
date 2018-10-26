#!/usr/bin/env python3
import cgi
import csv

form = cgi.FieldStorage()
nombre = form.getvalue('nombre')
legajo = form.getvalue('legajo')
sexo = form.getvalue('sexo')
edad = form.getvalue('edad')
password = form.getvalue('password')
with open('bd.csv', 'a', newline='') as csvfile:
    fieldnames = ['nombre', 'legajo', 'sexo', 'edad', 'password']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames) #DictWiter es un escritor normal como writer pero que asigna diccionarios
    writer.writerow({'nombre': nombre, 'legajo': legajo, 'sexo':sexo, 'edad':edad, 'password':password})
    

print("Content-type: text/html\n\n")
print("<html><head><title>CGI</title></head>")
print("<body>")
print("<font color = blue>\n")
print("<TITLE>CGI script output</TITLE>")
print("<h1 style=\"TEXT-ALIGN: center\">Exito !</h1>\n")
print("</font>\n")
print("</body>")
print("</html>")
