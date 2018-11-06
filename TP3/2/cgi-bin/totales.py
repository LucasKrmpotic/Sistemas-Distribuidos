#!/usr/bin/env python3
import cgi
import csv
import os
from models.alumno import Alumno
from utils.form import table_totales

if os.environ["REQUEST_METHOD"] == "GET":

    totales = Alumno.get_totales()

    table_body = "<tr class=\"table-light\">"
    table_body += "<td>Mujeres</td>"
    table_body += "<td>{}</td>".format(totales["mujeres1"]) 
    table_body += "<td>{}</td>".format(totales["mujeres2"]) 
    table_body += "<td>{}</td>".format(totales["mujeres3"])
    table_body += "</tr>"

    table_body += "<td>Varones</td>"
    table_body += "<td>{}</td>".format(totales["varones1"]) 
    table_body += "<td>{}</td>".format(totales["varones2"]) 
    table_body += "<td>{}</td>".format(totales["varones3"])
    table_body += "</tr>"

    table_body += "<td>Otros</td>"
    table_body += "<td>{}</td>".format(totales["otro1"]) 
    table_body += "<td>{}</td>".format(totales["otro2"]) 
    table_body += "<td>{}</td>".format(totales["otro3"])
    table_body += "</tr>"

    print("Content-Type: text/html; charset=utf-8\n\r")
    print()
    print(table_totales(table_body))