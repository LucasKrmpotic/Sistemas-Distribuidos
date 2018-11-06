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

def table(table_body):

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