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