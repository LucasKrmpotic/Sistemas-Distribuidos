#!/usr/bin/env python3
import cgi
import csv
import pandas as pd
import sys, os
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
    print('Status: 200 OK')
    print("Content-Type: text/html; charset=utf-8\n\r")
    print()
    print("<h1>Formilario de modificacion</h1>")   

