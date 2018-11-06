import pandas as pd
import sys, os
from http import cookies

SESSIONS_FILE = 'sessiones.csv'
MODEL_FILE = 'alumnos.csv'

class Alumno():

    def __init__(self, nombre, legajo, sexo, edad, password=None):
        self.nombre = nombre
        self.legajo = legajo
        self.sexo = sexo
        self.edad = edad
        self.password = password

    @classmethod
    def get_from_cookie(cls):
        cookie = cookies.SimpleCookie(os.environ["HTTP_COOKIE"])

        sessiones = pd.read_csv(SESSIONS_FILE)
        session = sessiones[sessiones['cookie'] == int(cookie['session'].value)]

        alumnos = pd.read_csv(MODEL_FILE)
        alumno = alumnos[alumnos['legajo'] == session.get_value(0, 'legajo')]

        return Alumno(
            alumno.at[0, 'nombre'],
            alumno.at[0, 'legajo'],
            alumno.at[0, 'sexo'],
            alumno.at[0, 'edad'],
            alumno.at[0, 'password']
        )
    
    def save(self):
        alumnos = pd.read_csv(MODEL_FILE)

        if (len(alumnos[alumnos["legajo"] == self.legajo])) > 0:
            raise Exception("El alumno ya se encuentra registrado")
        else:
            alumnos.loc[len(alumnos)] = [
                self.nombre,
                self.legajo,
                self.sexo,
                self.edad,
                self.password
            ] 
            alumnos.to_csv(MODEL_FILE, index=False)

    def update(self):
        alumnos = pd.read_csv(MODEL_FILE)

        if (len(alumnos[alumnos["legajo"] == self.legajo])) < 1:
            raise Exception("El alumno no se encuentra registrado")
        else:
            alumnos.loc[alumnos["legajo"] == self.legajo] = [
                self.nombre,
                self.legajo,
                self.sexo,
                self.edad,
                self.password
            ]
            alumnos.to_csv(MODEL_FILE, index=False)