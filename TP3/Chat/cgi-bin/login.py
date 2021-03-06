#!/usr/bin/env python3
import cgi
import csv
import hashlib
import base64
import sys, os
from models.session import Session
from models.message import Message
from views.chat_view import chat_view

if os.environ["REQUEST_METHOD"] == "POST":
    form = cgi.FieldStorage()
    nickname = form.getvalue('nickname')

    session = Session(nickname)
    session.last_msg = Message.get_last_msg_id()
    session.save()

    print("Status: 200 OK")
    print("Content-type: text/html")
    print(session.cookie.output())
    print()
    print(chat_view(nickname))

elif os.environ["REQUEST_METHOD"] == "GET":

    print("Location: /login.html")
    print()