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
        messages = Message.get_messages(session.last_msg+1)
        
        if messages is None:
            print("Status: 404 Not Found")
            print("Content-Type: text/html; charset=utf-8\n\r")
            print()

        else:
            last_msg_id = Message.get_last_msg_id()
            session.update(last_msg_id)
            
            result = ""

            for i in range(len(messages)):
                if messages[i][0]  == session.nickname:
                    result += """
                        <li class="sent">            
                            <span><small>{}</small><span></br><p>{}</p>
                        </li>
                    """.format(messages[i][0], messages[i][1])
                else:
                    result += """
                    <li class="replies">            
                        <span><small>{}</small><span></br><p>{}</p>
                    </li>
                    """.format(messages[i][0], messages[i][1])
            
            print("Content-Type: text/html; charset=utf-8\n\r")
            print()
            print(result)

    else: 
        print("Status: 403 Forbidden")
        print("Content-Type: text/html; charset=utf-8\n\r")
        print()

elif os.environ["REQUEST_METHOD"] == "POST":
    
    form = cgi.FieldStorage()
    text = form.getvalue('message')
    session = Session.get_current_session()

    message = Message(session.nickname, text)
    message.save()

    last_msg_id = Message.get_last_msg_id()
    session.update(last_msg_id)

    print("Content-Type: text/html; charset=utf-8\n\r")
    print()
    