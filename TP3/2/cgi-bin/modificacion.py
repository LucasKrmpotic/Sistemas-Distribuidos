#!/usr/bin/env python3
import cgi
import csv
import pandas as pd
import sys, os
import base64
import hashlib
from http import cookies
from utils.form import form_login, form_modificacion
from utils.authenticate import is_authenticated
from models.alumno import Alumno

if os.environ["REQUEST_METHOD"] == "GET":
    if is_authenticated():

        alumno = Alumno.get_from_cookie()

        print("Content-Type: text/html; charset=utf-8\n\r")
        print()
        print(form_modificacion(
            alumno.nombre,
            alumno.legajo,
            alumno.sexo,
            alumno.edad
        ))

    else: 
        print("Content-Type: text/html; charset=utf-8\n\r")
        print()
        print(form_login())

elif os.environ["REQUEST_METHOD"] == "POST":
    
    alumno = Alumno.get_from_cookie()

    form = cgi.FieldStorage()
    nombre = form.getvalue('nombre')
    sexo = form.getvalue('sexo')
    edad = int(form.getvalue('edad'))
    passwd = form.getvalue('password')
    

    if passwd is not None:
        password = str(base64.b64encode(hashlib.md5(passwd.encode('utf8')).digest()).decode("utf8"))
        if password != alumno.password:
            alumno.password = password
            
    if nombre != alumno.nombre:
        alumno.nombre = nombre
    if sexo != alumno.sexo:
        alumno.sexo = sexo
    if edad != alumno.edad:
        alumno.edad = edad

    try:
        alumno.update()
        status = "Status: 200 OK"
        respuesta = " Alumno actualizado exitosamente "
    except Exception as e:
        status = "Status: 400 Bab Request"
        respuesta = str(e)
    
    print(status)
    print("Content-Type: text/html; charset=utf-8\n\r")
    print()
    print("<h3>{}</h3>".format(respuesta))   

