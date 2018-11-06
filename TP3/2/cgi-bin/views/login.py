def login_view():

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