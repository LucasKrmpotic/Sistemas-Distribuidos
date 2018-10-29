#!/usr/bin/env python3
import cgi
import csv
import pandas as pd

form = cgi.FieldStorage()
nombre = form.getvalue('nombre')
legajo = form.getvalue('legajo')
sexo = form.getvalue('sexo')
edad = form.getvalue('edad')
password = form.getvalue('password')

alumno = [nombre, legajo, sexo, edad, password]

alumnos = pd.read_csv('alumnos.csv')

texto_respuesta = ""

if len(alumnos[alumnos["legajo"] == int (legajo)]) > 0:
    texto_respuesta = " El alumno ya se encuentra registrado "
else:
    texto_respuesta = " Exito ! "
    alumnos.loc[len(alumnos)] = alumno 
    alumnos.to_csv('alumnos.csv', index=False)

print("Content-type: text/html\n\n")
print("<html><head><title>CGI</title></head>")
print("<body>")
print(texto_respuesta)
print("</body>")
print("</html>") 