import pandas as pd
import sys, os
from http import cookies
import datetime
from random import randrange

SESSIONS_FILE = 'sessiones.csv'

class Session():

    def __init__(self, legajo, cookie=None):
        self.legajo = legajo
        if cookie is not None:
            self.cookie = cookie
        else:
            self.cookie = self._new_cookie()

    def save(self):
        sessiones = pd.read_csv(SESSIONS_FILE)
        sesion = [len(sessiones), str(self.cookie['session'].value), self.legajo]
        sessiones.loc[len(sessiones)] = sesion 
        sessiones.to_csv(SESSIONS_FILE, index=False)

    @classmethod
    def get_current_session(cls):

        cookie = cookies.SimpleCookie(os.environ["HTTP_COOKIE"])

        sessiones = pd.read_csv(SESSIONS_FILE, index_col="id")
        session = sessiones[sessiones['cookie'] == int(cookie['session'].value)]  

        legajo = session.get_value(0, 'legajo')
        return Session(legajo, cookie)      

    @classmethod
    def exists(cls):
        if "HTTP_COOKIE" in os.environ:
            cookie = cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
            if 'session' in cookie and cookie['session'].value:
                return True
        return False

    def _new_cookie(self):
        expiration = datetime.datetime.now() + datetime.timedelta(days=2)
        cookie = cookies.SimpleCookie()
        cookie["session"] = str(randrange(1000000000))
        cookie["session"]["domain"] = "localhost"
        cookie["session"]["path"] = "/"
        cookie["session"]["expires"] = expiration.strftime("%a, %d-%b-%Y %H:%M:%S GTM")

        return cookie

    def delete_cookie(self):

        cookie = cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
        sessiones = pd.read_csv(SESSIONS_FILE, index_col="id")
        session = sessiones[sessiones['cookie'] == int(cookie['session'].value)]
        sessiones.drop(session.index[0], inplace=True)
        sessiones.to_csv(SESSIONS_FILE)

        expiration = datetime.datetime.now() + datetime.timedelta(days=-1)
        cookie = cookies.SimpleCookie()
        cookie["session"] = ""
        cookie["session"]["domain"] = "localhost"
        cookie["session"]["path"] = "/"
        cookie["session"]["expires"] = expiration.strftime("%a, %d-%b-%Y %H:%M:%S GTM")
        return cookie