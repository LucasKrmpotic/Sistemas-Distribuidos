#!/usr/bin/env python3
from http import cookies
import cgi
import csv
import os


def is_authenticated():

    if "HTTP_COOKIE" in os.environ:
        cookie = cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
        if 'session' in cookie and cookie['session'].value:
            return True
    return False



