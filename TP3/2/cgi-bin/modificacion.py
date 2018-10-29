#!/usr/bin/env python3
<<<<<<< HEAD
nombre = form.getvalue('nombre')
legajo_desde= form.getvalue('legajo-desde')
legajo_hasta = form.getvalue('legajo-hasta')
sexo = form.getvalue('sexo')
edad_desde = form.getvalue('edad-desde')
edad_hasta = form.getvalue('edad-hasta')


alumnos = pd.read_csv('alumnos.csv')

alumnos_result = alumnos[(alumnos['nombre'] == nombre) | ( str(alumnos['sexo']) == sexo) | \
                         ((alumnos['legajo'] >= int(legajo_desde)) & (alumnos['legajo'] <= int(legajo_hasta))) | \
                         ((alumnos['edad'] >= int(edad_desde)) & (alumnos['edad'] <= int(edad_hasta)))]


table_body = ""
for alumno in alumnos_result:
    table_body += "<tr>" + "<td>" + alumno['nombre'] + "</td>" 
    table_body += "<td>" + alumno['legajo'] + "</td>"
    table_body += "<td>" + alumno['sexo'] + "</td>"
    table_body += "<td>" + alumno['edad'] + "</td>"
    table_body += "</tr>"
=======
import cgi
import csv
from http import cookies
import random
import pandas as pd

form = cgi.FieldStorage()
legajo = form.getvalue('legajo')
password = form.getvalue('password')

# legajo = 123
# password = "asdasd"
print("Content-type: text/html\n\n")
print("<html><head><title>CGI</title></head>")
print("<body>")
print(legajo + "  " + password)
print("</body>")
print("</html>") 

logeo = False
with open('alumnos.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    logeo = False
    for row in reader:
        # print(row['legajo'])
        # print(legajo)
        if ((row['legajo']) == str(legajo)):
            if(row['password'] == password):
                logeo = True
                nombre = row['nombre']
                edad = row['edad']

# df = pd.read_csv('alumnos.csv')
# print(df)
# try:
#     if((df.loc['legajo'] == legajo) and (df.loc['password'] == password)):
#         logeo = True
# except KeyError:  # Esta ejecutando el Except
#     print("Error")


if (logeo):
    #cookie=cookies.SimpleCookie()
    #ver lo de la cookie
    print("Content-type: text/html\n\n")
    print("<html><head><title>CGI</title></head>")
    print("<body>")
    print("Logueado")
    print("</body>")
    print("</html>") 
else:
    #caso de fallo
    print("Content-type: text/html\n\n")
    print("<html><head><title>CGI</title></head>")
    print("<body>")
    print("Error en Login")
    print("</body>")
    print("</html>") 
>>>>>>> 2c87a55e1946260f053223ca8c209fc4a581bc44
