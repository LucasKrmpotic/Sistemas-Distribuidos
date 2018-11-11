import pandas as pd
import sys, os
from http import cookies
import datetime
from random import randrange

SESSIONS_FILE = 'sessions.csv'

class Session():

    def __init__(self, nickname, cookie=None, last_msg=None, pk=None):
        self.nickname = nickname
        self.last_msg = last_msg
        if cookie is not None:
            self.cookie = cookie
            self.id = pk
        else:
            self.cookie = self._new_cookie()

    def save(self):
        #TODO:excepcion si existe nickname
        sessiones = pd.read_csv(SESSIONS_FILE)

        sesion = [len(sessiones), self.nickname, str(self.cookie['session'].value), self.last_msg]
        sessiones.loc[len(sessiones)] = sesion 
        
        sessiones.to_csv(SESSIONS_FILE, index=False)


    def update(self, last_msg):
        sessiones = pd.read_csv(SESSIONS_FILE)

        sessiones.loc[sessiones["nickname"] == self.nickname] = [
            self.id,
            self.nickname,
            self.cookie['session'].value,
            last_msg
        ]
        sessiones.to_csv(SESSIONS_FILE, index=False)

    @classmethod
    def get_users(cls, nickname):

        sessiones = pd.read_csv(SESSIONS_FILE)
        users = sessiones[sessiones['nickname'] != nickname]

        return users['nickname']

    @classmethod
    def get_current_session(cls):

        cookie = cookies.SimpleCookie(os.environ["HTTP_COOKIE"])

        sessiones = pd.read_csv(SESSIONS_FILE, index_col="id")
        session = sessiones[sessiones['cookie'] == cookie['session'].value]  
        if len(session) == 0:
            raise Exception("No existe la sesion")

        pk = sessiones.index[sessiones['cookie'] == cookie['session'].value].tolist()

        nickname = sessiones.at[pk[0], 'nickname']
        last_msg = sessiones.at[pk[0], 'lastmsg']

        return Session(nickname, cookie, last_msg, pk)      

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
        cookie["session"] = str(randrange(1000000000))  + "|" + self.nickname
        # cookie["session"] = str(randrange(1000000000))
        cookie["session"]["domain"] = "localhost"
        cookie["session"]["path"] = "/"
        cookie["session"]["expires"] = expiration.strftime("%a, %d-%b-%Y %H:%M:%S GTM")

        return cookie

    def delete_cookie(self):

        cookie = cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
        sessiones = pd.read_csv(SESSIONS_FILE, index_col="id")
        session = sessiones[sessiones['cookie'] == cookie['session'].value]
        sessiones.drop(session.index[0], inplace=True)
        sessiones.to_csv(SESSIONS_FILE)

        expiration = datetime.datetime.now() + datetime.timedelta(days=-1)
        cookie = cookies.SimpleCookie()
        cookie["session"] = ""
        cookie["session"]["domain"] = "localhost"
        cookie["session"]["path"] = "/"
        cookie["session"]["expires"] = expiration.strftime("%a, %d-%b-%Y %H:%M:%S GTM")
        return cookie