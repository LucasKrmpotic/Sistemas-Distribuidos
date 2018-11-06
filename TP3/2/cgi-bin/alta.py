#!/usr/bin/env python3
import cgi
import csv
import hashlib
import base64
import pandas as pd
import sys, os
from utils.form import form_alta
from models.alumno import Alumno


if os.environ["REQUEST_METHOD"] == "GET":

    print("Content-Type: text/html; charset=utf-8\n\r")
    print()
    print(form_alta())

if os.environ["REQUEST_METHOD"] == "POST":

    form = cgi.FieldStorage()
    nombre = form.getvalue('nombre')
    legajo = int(form.getvalue('legajo'))
    sexo = form.getvalue('sexo')
    edad = int(form.getvalue('edad'))
    password = str(base64.b64encode(hashlib.md5(form.getvalue('password').encode('utf8')).digest()).decode("utf8"))

    alumno = Alumno(nombre, legajo, sexo, edad, password)
    try:
        alumno.save()
        status = "Status: 200 OK"
        respuesta = " Alumno registrado exitosamente "

    except Exception as e:
        status = "Status: 400 Bab Request"
        respuesta = str(e)
    
    print(status)
    print("Content-Type: text/html; charset=utf-8\n\r")
    print()
    print("<h3>{}</h3>".format(respuesta))

