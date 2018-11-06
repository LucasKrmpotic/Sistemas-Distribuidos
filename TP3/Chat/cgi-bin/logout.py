#!/usr/bin/env python3
import os
import cgi
from http import cookies
from models.session import Session

if Session.exists():

    session = Session.get_current_session()
    cookie = session.delete_cookie()
    
    print(cookie.output())
    print("Content-Type: text/html; charset=utf-8\n\r")
    print()

else:
    print("Content-Type: text/html; charset=utf-8\n\r")
    print("Location: / ")
    print()