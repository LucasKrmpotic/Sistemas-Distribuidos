#!/usr/bin/env python3
import cgi
import csv
from http import cookies
import random

# form = cgi.FieldStorage()
# legajo = form.getvalue('legajo')
# password = form.getvalue('password')

# with open('bd.csv', 'r') as csvfile:
#     reader = csv.DictReader(csvfile)
#     logeo = False
#     for row in reader:
#         if (row['legajo'] == legajo and row['password'] == password):
#             logeo = True
#             nombre = row['nombre']
#             edad = row['edad']
#             sexo = row['sexo']

with open('bd.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    logeo = False
    for row in reader:
        print(row)


if (logeo):
    cookie=cookies.SimpleCookie()
    cookie['login']=str(random.randint(0,500)) #asigno la cookie
    # Aca la parte de la modificacion
else:
    #caso de fallo
    print("Content-type: text/html\n\n")
    print("<html><head><title>CGI</title></head>")
    print("<body>")
    print("El nombre y/o password NO son correctos")
    print("</body>")
    print("</html>") 