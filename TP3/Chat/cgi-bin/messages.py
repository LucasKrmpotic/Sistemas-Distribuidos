#!/usr/bin/env python3
import cgi
import csv
import pandas as pd
import sys, os
from http import cookies
from models.session import Session
from models.message import Message

if os.environ["REQUEST_METHOD"] == "GET":

    if Session.exists():

        session = Session.get_current_session()
        messages = Message.get_messages(session.last_msg)

        
        print("Content-Type: text/html; charset=utf-8\n\r")
        print()
        print(messages)

    else: 
        print("Status: 403 Forbidden")
        print("Content-Type: text/html; charset=utf-8\n\r")
        print("/login.html")
        print()

elif os.environ["REQUEST_METHOD"] == "POST":
    
    form = cgi.FieldStorage()
    text = form.getvalue('message')
    session = Session.get_current_session()

    message = Message(session.nickname, text)
    message.save()

    print("Content-Type: text/html; charset=utf-8\n\r")
    print()
    print("<h1>Mensaje: {}, usuario {}, id de mensaje {}".format(message.text, message.user, message.id))