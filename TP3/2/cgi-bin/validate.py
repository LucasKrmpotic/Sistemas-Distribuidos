#!/usr/bin/env python3
from http import cookies
import cgi
import csv
import os
from shared.header import header
from shared.footer import footer

form = cgi.FieldStorage()
leg = form.getvalue('legajo')
psw = form.getvalue('password')

try:

    if "HTTP_COOKIE" in os.environ:
        cookie = cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
        if 'session' in cookie:
            if cookie['session'].value:
                print("Content-type: text/html")
                print()
                print(header())
                print("<h1>{}</h1>".format(cookie['session'].value))
                print(footer())
    else:
        print("Content-type: text/html")
        print("Location:{}".format("/login.html"))        
        print()
except:
    print("Content-type: text/html")
    print("Location:{}".format("/login.html"))        
    print()
