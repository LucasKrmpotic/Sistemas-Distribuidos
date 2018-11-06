#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def form_alta():
	return """
	<div class="row justify-content-md-center">
	<div class="col-md-8">
		<form id="form-alta">
			<fieldset>
			<legend>Alta de alumno</legend>
			<div class="form-group">
				<label for="nombre">Nombre y Apellido</label>
				<input class="form-control" name="nombre" placeholder="Apellido y nombre" type="text" required>
				<small class="form-text text-muted">Ingrese su apellido seguido de su nombre.</small>
			</div>

			<div class="form-group">
				<label for="legajo">N&uacute;mero de legajo</label>
				<input class="form-control" name="legajo" placeholder="Numero de legajo" type="text" required>
				<small class="form-text text-muted">Ingrese su n&uacute;mero de legajo.</small>
			</div>

			<fieldset class="form-group">
				<legend>Sexo</legend>
				<div class="form-check">
				<label class="form-check-label">
					<input class="form-check-input" name="sexo" value="masculino" type="radio"> Masculino
				</label>
				</div>
				<div class="form-check">
				<label class="form-check-label">
					<input class="form-check-input" name="sexo" value="femenino" type="radio"> Femenino
				</label>
				</div>
				<div class="form-check">
				<label class="form-check-label">
					<input name="sexo" class="form-check-input" value="otro" checked="" type="radio"> Otro
				</label>
				</div>
			</fieldset>

			<div class="form-group">
				<label for="edad">Edad</label>
				<input class="form-control" name="edad" placeholder="Edad desde" type="text" required>
				<small class="form-text text-muted">Ingrese la edad.</small>
			</div>

			<div class="form-group">
				<label for="password">Password</label>
				<input name="password" class="form-control" placeholder="Password" type="password">
			</div>
			<button type="submit" onclick="post_alta()" class="btn btn-primary">Enviar</button>
			</fieldset>
		</form>
	</div>
	</div>
		"""

def form_modificacion(nombre, legajo, sexo, edad):
	formulario = """
	<div class="row justify-content-md-center">
	<div class="col-md-8">
		<form id="form-modificacion">
			<fieldset>
			<legend>Modificaci&oacute;n de datos</legend>

			<div class="form-group">
				<label for="nombre">Nombre y Apellido</label>
				<input class="form-control" name="nombre" value="{}" type="text">
				<small class="form-text text-muted">Ingrese su apellido seguido de su nombre.</small>
			</div> 

			<div class="form-group">
				<label for="legajo">N&uacute;mero de legajo</label>
				<input class="form-control" name="legajo" value="{}" readonly=True type="text">
				<small class="form-text text-muted">Ingrese su n&uacute;mero de legajo.</small>
			</div>

			<fieldset class="form-group">
				<legend>Sexo</legend>

				<div class="form-check">
				<label class="form-check-label">
					<input class="form-check-input" name="sexo" value="masculino" {} type="radio"> Masculino
				</label>
				</div>

				<div class="form-check">
				<label class="form-check-label">
					<input class="form-check-input" name="sexo" value="femenino" {} type="radio"> Femenino
				</label>
				</div>

				<div class="form-check">
				<label class="form-check-label">
					<input name="sexo" class="form-check-input" value="otro" {} type="radio"> Otro
				</label>
				</div>

			</fieldset>

			<div class="form-group">
				<label for="edad">Edad</label>
				<input class="form-control" name="edad" value="{}" type="text">
				<small class="form-text text-muted">Ingrese la edad.</small>
			</div>
			
			<div class="form-group">
				<label for="password">Password</label>
				<input name="password" class="form-control" placeholder="Password" type="password">
			</div>

			<button type="submit" onclick="post_modificacion()" class="btn btn-primary">Enviar</button>
			</fieldset>
		</form>
	</div>
	</div>
	"""

	if sexo == "masculino":
		return formulario.format(nombre, legajo, "checked=\"\"", "", "", edad)
	elif sexo == "femenino":
		return formulario.format(nombre, legajo, "", "checked=\"\"", "", edad)
	elif sexo == "otro":
		return formulario.format(nombre, legajo, "", "", "checked=\"\"", edad)

def form_login():

    return """
	<div class="row justify-content-md-center">
	<div class="col-md-8">
        <form id="form-login">
          <fieldset>
            <legend>Login</legend>

            <div class="form-group">
              <label for="legajo">N&uacutemero de legajo</label>
              <input class="form-control" name="legajo" placeholder="Numero de legajo" type="text" required>
              <small class="form-text text-muted">Ingrese su n&uacutemero de legajo.</small>
            </div>

            <div class="form-group">
              <label for="password">Password</label>
				<input name="password" class="form-control" placeholder="Password" type="password">
            </div>

            <button type="submit" onclick="login()" class="btn btn-primary">Enviar</button>
          </fieldset>
        </form>
	</div>
	</div>
    """

def form_consulta():

		return """
    <div class="row justify-content-md-center">
      <div class="col-md-6">
        <form id="form-consulta">
          <fieldset>
			<legend>B&uacute;squeda de alumnos</legend>
            <div class="form-group">
              <label for="nombre">Nombre y Apellido</label>
              <input class="form-control" name="nombre" aria-describedby="emailHelp" placeholder="Apellido y nombre" type="text" required>
              <small class="form-text text-muted">Ingrese su apellido seguido de su nombre.</small>
            </div>

            <div class="form-group">
              <label for="legajo-desde">N&uacute;mero de legajo</label>
              <input class="form-control" name="legajo-desde" aria-describedby="emailHelp" placeholder="Legajo m&iacute;nimo" type="text" required>
              <small class="form-text text-muted">Legajo m&iacute;nimo.</small>
              <input class="form-control" name="legajo-hasta" aria-describedby="emailHelp" placeholder="Legajo m&aacute;ximo" type="text" required>
              <small class="form-text text-muted">Legajo m&aacute;ximo.</small>
            </div>

            <fieldset class="form-group">
              <legend>Sexo</legend>

              <div class="form-check">
                <label class="form-check-label">
                  <input class="form-check-input" name="sexo" id="optionsRadios1" value="masculino" checked="" type="radio"> Masculino
                </label>
              </div>

              <div class="form-check">
                <label class="form-check-label">
                  <input class="form-check-input" name="sexo" id="optionsRadios1" value="femenino" checked="" type="radio"> Femenino
                </label>
              </div>

              <div class="form-check">
                <label class="form-check-label">
                  <input class="form-check-input" name="sexo" id="optionsRadios1" value="otro" checked="" type="radio"> Otro
                </label>
              </div>

            </fieldset>

            <div class="form-group">
              <label for="edad-desde">Edad</label>
              <input class="form-control" name="edad-desde" aria-describedby="emailHelp" placeholder="Edad desde" type="text" required>
              <small class="form-text text-muted">Ingrese edad m&iacute;nima.</small>
              <input class="form-control" name="edad-hasta" aria-describedby="emailHelp" placeholder="Edad hasta" type="text" required>
              <small class="form-text text-muted">Ingrese edad m&aacute;xima.</small>
            </div>

            <button type="submit" onclick="post_consulta()" class="btn btn-primary">Enviar</button>
          </fieldset>


        </form>
      </div>
    </div>
		"""

def print_table(table_body):

	return """
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
  <tbody>{}</tbody>
        </table>
        </div>
        </div>
        </div>
""".format(table_body)


def table_totales(table_body):

	return """
<div class="container">
<div class="row justify-content-md-center">
    <div class="col-md-8">
    <h2 style="text-align: center; margin-top:1em;">Totales por sexo y grupo etario</h2>
    </div>
</div>
<div class="row justify-content-md-center">
<div class="col-md-10">
<table class="table table-hover" style="margin-top:1em;">
  <thead>
    <tr>
      <th scope="col">Sexo</th>
      <th scope="col">[0..20]</th>
      <th scope="col">[21..40]</th>
      <th scope="col">[41..]</th>
    </tr>
  </thead>
  <tbody>{}</tbody>
        </table>
        </div>
        </div>
        </div>
""".format(table_body)