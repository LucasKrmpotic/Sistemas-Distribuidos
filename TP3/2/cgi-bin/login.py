#!/usr/bin/env python3
import cgi
import csv
import hashlib
import base64
import sys, os
from models.alumno import Alumno
from models.session import Session
from views.login import login_view


if os.environ["REQUEST_METHOD"] == "GET":
    
    print("Content-type: text/html")
    print(login_view())
    print()   

elif os.environ["REQUEST_METHOD"] == "POST":
    form = cgi.FieldStorage()
    legajo = int(form.getvalue('legajo'))
    password = str(base64.b64encode(hashlib.md5(form.getvalue('password').encode('utf8')).digest()).decode("utf8"))

    alumno = Alumno.get_by_legajo(legajo)
    if alumno.check_pass(password):

        session = Session(alumno.legajo)
        session.save()

        print("Status: 200 OK")
        print("Content-type: text/html")
        print(session.cookie.output())
        print()
        print("<h3>Te has logueado exitosamente</h3>")
    else:
        print("Status: 400 Bab Request")
        print("Content-type: text/html")
        print()
        print("<h3>Usuario o contrase&ntilde;a intorrectos</h3>")
