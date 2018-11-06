#!/usr/bin/env python3
import cgi
import csv
import os
import pandas as pd
from views.consultas import form_consulta, table
from models.alumno import Alumno

if os.environ["REQUEST_METHOD"] == "GET":

    print("Content-Type: text/html; charset=utf-8\n\r")
    print()
    print(form_consulta())

elif os.environ["REQUEST_METHOD"] == "POST":

    form = cgi.FieldStorage()
    nombre = form.getvalue('nombre')
    legajo_desde= int(form.getvalue('legajo-desde'))
    legajo_hasta = int(form.getvalue('legajo-hasta'))
    sexo = form.getvalue('sexo')
    edad_desde = int(form.getvalue('edad-desde'))
    edad_hasta = int(form.getvalue('edad-hasta'))

    alumnos_result = Alumno.filter_by(nombre, legajo_desde, legajo_hasta, sexo, edad_desde, edad_hasta)    

    table_body = ""

    for i in range(0, len(alumnos_result)):
        table_body += "<tr class=\"table-light\">"
        table_body += "<td>{}</td>".format(alumnos_result.get_value(i, 'nombre'))
        table_body += "<td>{}</td>".format(alumnos_result.get_value(i, 'legajo')) 
        table_body += "<td>{}</td>".format(alumnos_result.get_value(i, 'sexo')) 
        table_body += "<td>{}</td>".format(alumnos_result.get_value(i, 'edad'))
        table_body += "</tr>"

    print("Content-Type: text/html; charset=utf-8\n\r")
    print()
    print(table(table_body))