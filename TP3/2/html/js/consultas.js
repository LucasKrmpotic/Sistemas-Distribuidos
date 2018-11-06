function get_consultas(){

    container = $('#main-container')

    $.ajax({
      method: "GET",
      url: "/cgi-bin/consultas.py"
    })
    .done(function (res) {
      container.html(res)
    })
    .fail(function (err) {
        $('#error-msg').html(err.responseText);
        $('#alertError').removeAttr("hidden");
    });

}

function post_consulta(){

    container = $('#main-container')

    $('#form-consulta').submit(function (event) {
  
        var $this = $(this);
        var frmValues = $this.serialize();
        
        $.ajax({
            method: "POST",
            url: "/cgi-bin/consultas.py",
            data: frmValues
        })
        .done(function (res) {
            container.html(res);
        })
        .fail(function (err) {
            $('#error-msg').html(err.responseText);
            $('#alertError').removeAttr("hidden");
        });
        event.preventDefault(); 
    });
}