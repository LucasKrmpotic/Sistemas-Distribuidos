#!/usr/bin/env python3
nombre = form.getvalue('nombre')
legajo_desde= form.getvalue('legajo-desde')
legajo_hasta = form.getvalue('legajo-hasta')
sexo = form.getvalue('sexo')
edad_desde = form.getvalue('edad-desde')
edad_hasta = form.getvalue('edad-hasta')


alumnos = pd.read_csv('alumnos.csv')

alumnos_result = alumnos[(alumnos['nombre'] == nombre) | ( str(alumnos['sexo']) == sexo) | \
                         ((alumnos['legajo'] >= int(legajo_desde)) & (alumnos['legajo'] <= int(legajo_hasta))) | \
                         ((alumnos['edad'] >= int(edad_desde)) & (alumnos['edad'] <= int(edad_hasta)))]


table_body = ""
for alumno in alumnos_result:
    table_body += "<tr>" + "<td>" + alumno['nombre'] + "</td>" 
    table_body += "<td>" + alumno['legajo'] + "</td>"
    table_body += "<td>" + alumno['sexo'] + "</td>"
    table_body += "<td>" + alumno['edad'] + "</td>"
    table_body += "</tr>"
