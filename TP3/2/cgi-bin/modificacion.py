#!/usr/bin/env python3
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
