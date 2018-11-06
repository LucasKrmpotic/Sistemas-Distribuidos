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