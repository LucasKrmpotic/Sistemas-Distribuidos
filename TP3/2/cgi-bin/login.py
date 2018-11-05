#!/usr/bin/env python3
from utils.session import new_cookie
import cgi
import csv
import hashlib
import base64
import pandas as pd
import sys, os



form = cgi.FieldStorage()
legajo = int(form.getvalue('legajo'))
password = str(base64.b64encode(hashlib.md5(form.getvalue('password').encode('utf8')).digest()).decode("utf8"))

alumnos = pd.read_csv('alumnos.csv')
alumno = alumnos[(alumnos['legajo'] == legajo)]
if len(alumno) > 0 and alumno.get_value(0, 'password') == password:

    cookie = new_cookie()

    sessiones = pd.read_csv('sessiones.csv')
    sesion = [str(cookie['session'].value), legajo]
    sessiones.loc[len(sessiones)] = sesion 
    sessiones.to_csv('sessiones.csv', index=False)

    print("Status: 200 OK")
    print("Content-type: text/html")
    print(cookie.output())
    print()
    print("<h3>Te has logueado exitosamente</h3>")
else:
    print("Status: 400 Bab Request")
    print("Content-type: text/html")
    print()
    print("<h3>Usuario o contrase&ntilde;a intorrectos</h3>")
