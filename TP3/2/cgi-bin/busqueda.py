#!/usr/bin/env python3
import cgi
import csv
import pandas as pd

form = cgi.FieldStorage()
nombre = form.getvalue('nombre')
legajo_desde= form.getvalue('legajo-desde')
legajo_hasta = form.getvalue('legajo-hasta')
sexo = form.getvalue('sexo')
edad_desde = form.getvalue('edad-desde')
edad_hasta = form.getvalue('edad-hasta')
# nombre = "maxi"
# legajo_desde= 10
# legajo_hasta = 121
# sexo = "masculino"
# edad_desde = 20
# edad_hasta = 29


alumnos = pd.read_csv('alumnos.csv')

alumnos_result = alumnos[(alumnos['nombre'] == nombre) | ( str(alumnos['sexo']) == sexo) | \
                         ((alumnos['legajo'] >= int(legajo_desde)) & (alumnos['legajo'] <= int(legajo_hasta))) | \
                         ((alumnos['edad'] >= int(edad_desde)) & (alumnos['edad'] <= int(edad_hasta)))]
# alumnos_result = alumnos[(alumnos['nombre'] == nombre) | ( str(alumnos['sexo']) == sexo) | \
#                           ((alumnos['legajo'] >= (legajo_desde)) & (alumnos['legajo'] <= (legajo_hasta))) | \
#                           ((alumnos['edad'] >= (edad_desde)) & (alumnos['edad'] <= (edad_hasta)))]

# table_body = ""
# for alumno in alumnos_result:
#     table_body = "<tr>"
#     table_body += "<td>" + alumno['nombre'] + "</td>" 
#     table_body += "<td>" + alumno['legajo'] + "</td>"
#     table_body += "<td>" + alumno['sexo'] + "</td>"
#     table_body += "<td>" + alumno['edad'] + "</td>"
#     table_body += "</tr>"
# print(table_body)


print("Content-type: text/html\n\n")
print("<html><head><title>CGI</title></head>")
print("<body>")
print("<table>")
<<<<<<< HEAD
print("<tr>")
print("<td>nombre</td><td>legajo</td><td>sexo</td><td>edad</td>")
print("</tr>")
print("<tr>")
print("<td>1</td><td>2</td><td>3</td><td>4</td>")
print("</tr>")
=======
print("<tr>")    
print("<td>Nombre</td><td>Legajo</td><td>Sexo</td><td>Edad</td>")
print("</tr>")
#print(table_body)
>>>>>>> 2c87a55e1946260f053223ca8c209fc4a581bc44
print("</table>")
print("</body>")
print("</html>")
