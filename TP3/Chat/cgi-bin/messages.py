#!/usr/bin/env python3
import cgi
import csv
import pandas as pd
import sys, os
from http import cookies


if os.environ["REQUEST_METHOD"] == "GET":

    if Session.exists():

        session = Session.get_current_session()


    else: 
        print("Content-Type: text/html; charset=utf-8\n\r")
        print("Location: / ")
        print()

elif os.environ["REQUEST_METHOD"] == "POST":
    pass