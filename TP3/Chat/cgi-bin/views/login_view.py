def login_view():

    return """
        <div class="login_wrapper">
          <div class="animate form login_form">
            <section class="login_content">
              <form id="form-login">
                <fieldset>
                  <legend>Ingreso a la sala de chat</legend>

                  <div class="form-group">
                    <label for="nickname">Nickname</label>
                    <input class="form-control" name="nickname" placeholder="Nickname" type="text" required>
                    <small class="form-text text-muted">Ingrese su nickname.</small>
                  </div>

                  <button type="submit" onclick="login()" class="btn btn-primary">Login</button>
                </fieldset>
              </form>

              <div class="separator">
                <div class="clearfix"></div>
                <br />
                <div>
                  <h1>
                    </i> Chat CGI</h1>
                  <p> Sistemas Distribuidos 2018</p>
                </div>
              </div>
            </section>
          </div>
        </div>
    """