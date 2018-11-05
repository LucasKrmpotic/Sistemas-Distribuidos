function get_modificacion() {
    container = $('#main-container')

    $.ajax({
      method: "GET",
      url: "/cgi-bin/modificacion.py"
    })
    .done(function (res) {
        container.html(res);
    })
    .fail(function (err) {
        console.log(err);
        
        $('#error-msg').html(err.responseText);
        $('#alertError').removeAttr("hidden");
    });
}