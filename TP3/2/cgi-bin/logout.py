#!/usr/bin/env python3
import os
import cgi
from session import delete_cookie
from http import cookies
from shared.footer import footer
from shared.header import header

try:
    cookie = cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
    
    if cookie['session'].value != "":        
        print("Content-type: text/html")
        print(delete_cookie())
        print("Location:{}".format("/login.html"))
        print()
    else:
        print("Content-type: text/html")
        print("Location:{}".format("/login.html"))        
        print()

except:
    print("Content-type: text/html")
    print("Location:{}".format("/login.html"))        
    print()



