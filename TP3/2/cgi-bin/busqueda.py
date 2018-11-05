#!/usr/bin/env python3
import cgi
import csv
import pandas as pd
from shared.footer import footer
from shared.header import header

form = cgi.FieldStorage()
nombre = form.getvalue('nombre')
legajo_desde= int(form.getvalue('legajo-desde'))
legajo_hasta = int(form.getvalue('legajo-hasta'))
sexo = form.getvalue('sexo')
edad_desde = int(form.getvalue('edad-desde'))
edad_hasta = int(form.getvalue('edad-hasta'))


alumnos = pd.read_csv('alumnos.csv')

alumnos_result = alumnos[(alumnos['nombre'] == nombre) | ( alumnos['sexo'] == sexo) | \
                         ((alumnos['legajo'] >= legajo_desde) & (alumnos['legajo'] <= legajo_hasta)) | \
                         ((alumnos['edad'] >= edad_desde) & (alumnos['edad'] <= edad_hasta))]

table_body = ""

for i in range(0, len(alumnos_result)):
    table_body += "<tr class=\"table-light\">"
    table_body += "<td>{}</td>".format(alumnos_result.get_value(i, 'nombre'))
    table_body += "<td>{}</td>".format(alumnos_result.get_value(i, 'legajo')) 
    table_body += "<td>{}</td>".format(alumnos_result.get_value(i, 'sexo')) 
    table_body += "<td>{}</td>".format(alumnos_result.get_value(i, 'edad'))
    table_body += "</tr>"


print(header())
print("""
<div class="container">
<div class="row justify-content-md-center">
    <div class="col-md-8">
    <h1 style="text-align: center; margin-top:1em;">Resultados de la busqueda</h1>
    </div>
</div>
<div class="row justify-content-md-center">
<div class="col-md-10">
<table class="table table-hover" style="margin-top:1em;">
  <thead>
    <tr>
      <th scope="col">Nombre</th>
      <th scope="col">Legajo</th>
      <th scope="col">Sexo</th>
      <th scope="col">Edad</th>
    </tr>
  </thead>
  <tbody>
""")
print(table_body)
print("""</tbody>
        </table>
        </div>
        </div>
        </div>
""")
print(footer())