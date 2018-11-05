#!/usr/bin/env python3
import os
from session.cookies import new_cookie
from shared.header import header
from shared.footer import footer
from shared.form import form_alta, form_modificacion

nombre = "Lucas"
legajo = "123"
edad = "30"
sexo="masculino"

print("Content-type: text/html")
print(new_cookie())
print()
print(header())
print(form_modificacion(nombre, legajo, sexo, edad))
print(footer())

