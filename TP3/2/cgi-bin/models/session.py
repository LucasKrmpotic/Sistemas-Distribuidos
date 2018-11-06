

class Session():

    def __init__(self, legajo):
        self.legajo = legajo
        self.cookie = self._new_cookie()



    def save(self):    


    def _new_cookie():
        expiration = datetime.datetime.now() + datetime.timedelta(days=2)
        cookie = cookies.SimpleCookie()
        cookie["session"] = str(randrange(1000000000))
        cookie["session"]["domain"] = "localhost"
        cookie["session"]["path"] = "/"
        cookie["session"]["expires"] = expiration.strftime("%a, %d-%b-%Y %H:%M:%S GTM")

        return cookie

    def delete_cookie():

        cookie = cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
        sessiones = pd.read_csv("/usr/local/apache2/cgi-bin/sessiones.csv", index_col="id")
        session = sessiones[sessiones['cookie'] == int(cookie['session'].value)]
        sessiones.drop(session.index[0], inplace=True)
        sessiones.to_csv("/usr/local/apache2/cgi-bin/sessiones.csv")

        expiration = datetime.datetime.now() + datetime.timedelta(days=-1)
        cookie = cookies.SimpleCookie()
        cookie["session"] = ""
        cookie["session"]["domain"] = "localhost"
        cookie["session"]["path"] = "/"
        cookie["session"]["expires"] = expiration.strftime("%a, %d-%b-%Y %H:%M:%S GTM")
        return cookie