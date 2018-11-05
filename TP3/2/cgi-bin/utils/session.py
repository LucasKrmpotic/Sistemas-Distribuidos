#!/usr/bin/env python3
from http import cookies
from random import randrange
import os
import base64
import datetime
import random

def new_cookie():
    expiration = datetime.datetime.now() + datetime.timedelta(days=2)
    cookie = cookies.SimpleCookie()
    cookie["session"] = str(randrange(1000000000))
    cookie["session"]["expires"] = expiration.strftime("%a, %d-%b-%Y %H:%M:%S GTM")
    return cookie

def delete_cookie():
    expiration = datetime.datetime.now() - datetime.timedelta(days=30)
    cookie = cookies.SimpleCookie()
    cookie["session"] = ""
    cookie["session"]["expires"] = expiration.strftime("%a, %d-%b-%Y %H:%M:%S GTM")
    return cookie