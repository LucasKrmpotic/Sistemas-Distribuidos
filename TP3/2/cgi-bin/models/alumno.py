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

    @classmethod
    def get_totales(cls):
        alumnos = pd.read_csv(MODEL_FILE)

        result = {
            "mujeres1":len(alumnos[(alumnos['sexo'] == "femenino") & (alumnos['edad'] < 21)]),
            "mujeres2":len(alumnos[(alumnos['sexo'] == "femenino") & ((alumnos['edad'] > 20) & (alumnos['edad'] < 41))]),
            "mujeres3":len(alumnos[(alumnos['sexo'] == "femenino") & (alumnos['edad'] > 40)]),
            "varones1":len(alumnos[(alumnos['sexo'] == "masculino") & (alumnos['edad'] < 21)]),
            "varones2":len(alumnos[(alumnos['sexo'] == "masculino") & ((alumnos['edad'] > 20) & (alumnos['edad'] < 41))]),
            "varones3":len(alumnos[(alumnos['sexo'] == "masculino") & (alumnos['edad'] > 40)]),
            "otro1":len(alumnos[(alumnos['sexo'] == "otro") & (alumnos['edad'] < 21)]),
            "otro2":len(alumnos[(alumnos['sexo'] == "otro") & ((alumnos['edad'] > 20) & (alumnos['edad'] < 41))]),
            "otro3":len(alumnos[(alumnos['sexo'] == "otro") & (alumnos['edad'] > 40)]),
        }

        return result

    @classmethod
    def filter_by(cls, nombre, legajo_desde, legajo_hasta, sexo, edad_desde, edad_hasta):

        alumnos = pd.read_csv(MODEL_FILE)

        return alumnos[(alumnos['nombre'] == nombre) | ( alumnos['sexo'] == sexo) | \
                        ((alumnos['legajo'] >= legajo_desde) & (alumnos['legajo'] <= legajo_hasta)) | \
                        ((alumnos['edad'] >= edad_desde) & (alumnos['edad'] <= edad_hasta))]

    
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