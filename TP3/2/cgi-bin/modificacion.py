#!/usr/bin/env python3
import cgi
import csv
import pandas as pd
import sys, os
import base64
import hashlib
from http import cookies
from views.modificacion import form_modificacion
from views.login import login_view
from models.alumno import Alumno
from models.session import Session

if os.environ["REQUEST_METHOD"] == "GET":

    if Session.exists():

        session = Session.get_current_session()
        alumno = Alumno.get_by_legajo(session.legajo)

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
        print(login_view())

elif os.environ["REQUEST_METHOD"] == "POST":
    
    session = Session.get_current_session()
    alumno = Alumno.get_by_legajo(session.legajo)

    form = cgi.FieldStorage()
    nombre = form.getvalue('nombre')
    sexo = form.getvalue('sexo')
    edad = int(form.getvalue('edad'))
    passwd = form.getvalue('password')
    

    if passwd is not None:
        password = str(base64.b64encode(hashlib.md5(passwd.encode('utf8')).digest()).decode("utf8"))
        if password != alumno.password:
            alumno.password = password
            
    if nombre!= alumno.nombre and nombre is not None:
        alumno.nombre = nombre
    if sexo != alumno.sexo and sexo is not None:
        alumno.sexo = sexo
    if edad != alumno.edad and edad is not None:
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

