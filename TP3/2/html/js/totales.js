function totales(){

    container = $('#main-container')

    $.ajax({
      method: "GET",
      url: "/cgi-bin/totales.py"
    })
    .done(function (res) {
      container.html(res)
    })
    .fail(function (err) {
        $('#error-msg').html(err.responseText);
        $('#alertError').removeAttr("hidden");
    });


}