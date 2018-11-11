#!/usr/bin/env python3
import cgi
import csv
import sys, os
from http import cookies

from models.session import Session
from views.chat_view import chat_view
from views.login_view import login_view


if os.environ["REQUEST_METHOD"] == "GET":

    if Session.exists():

        session = Session.get_current_session()

        print("Content-Type: text/html; charset=utf-8\n\r")
        print()
        print(chat_view(session.nickname))

    else:

        print("Content-Type: text/html; charset=utf-8\n\r")
        print()
        print(login_view())