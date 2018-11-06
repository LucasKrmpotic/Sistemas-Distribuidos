#!/usr/bin/env python3
import os
import cgi
from utils.session import delete_cookie
from utils.authenticate import is_authenticated
from http import cookies

if is_authenticated():

    cookie = delete_cookie()
    print(cookie.output())
    print("Content-Type: text/html; charset=utf-8\n\r")
    print()

else:
    print("Content-Type: text/html; charset=utf-8\n\r")
    print("Location: / ")
    print()
    


