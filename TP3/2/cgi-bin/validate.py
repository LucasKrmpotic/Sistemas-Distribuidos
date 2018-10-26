#!/usr/bin/env python3
from http import cookies
import cgi
import csv
import os

form = cgi.FieldStorage()
leg = form.getvalue('legajo')
psw = form.getvalue('password')

if ('HTTP_COOKIE') in os.environ:
    cookie_string=os.environ.get('HTTP_COOKIE')
    c=cookies.SimpleCookie()
    c.load(cookie_string)
    c['expires'] = 30*60 #cookie expira en media hora

    try:
        data = c['login'].value
        #validar aca :/
        print("Content-type: text/html\n\n")
        print("<html><head><title>CGI</title></head>")
        print("<body>")
        print("cookie data: "+data+"<br>")
        print("</body>")
        print("</html>")

    except KeyError:
        print("Ocurrio un error en la Cookie o la misma expiro...")
    
else:
    print( """
        <h1>Login</h1>
        <form method='GET' action="login.py">
          Legajo:<br>
          <input type="text" name="legajo"><br>
          Contrasenia:<br>
          <input type="password" name="password"><br>
          <br>
          <input type="submit" value="Aceptar">
        </form>
        """)
    print("</body>")    
    print("</html>")
