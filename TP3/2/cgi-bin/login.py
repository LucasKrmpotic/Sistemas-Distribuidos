#!/usr/bin/env python3
from session import new_cookie
from shared.header import header
from shared.footer import footer
import cgi
import csv
import pandas as pd

form = cgi.FieldStorage()
legajo = int(form.getvalue('legajo'))
password = form.getvalue('password')

alumnos = pd.read_csv('alumnos.csv')

if len(alumnos[(alumnos['legajo'] == legajo)]) > 0:
    print("Content-type: text/html")
    print(new_cookie())
    print()
    print(header())
    print("<h1>estas logueado</h1>")
    print(footer())
else:
    print("Content-type: text/html")
    print()
    print(header())
    print("<h1>NO estas logueado</h1>")
    print(footer())  
