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
        users = Session.get_users(session.nickname)
        
        result = ""

        for user in users:

            result += """
            <li class="contact">
                <div class="wrap">
                  <span class="contact-status online"></span>
                  <div class="meta">
                    <p class="name">{}</p>
                  </div>
                </div>
              </li>
            """.format(user)

        print("Content-Type: text/html; charset=utf-8\n\r")
        print()
        print(result)

    else: 
        print("Status: 403 Forbidden")
        print("Content-Type: text/html; charset=utf-8\n\r")
        print("/login.html")
        print()