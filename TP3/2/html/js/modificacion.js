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

function post_modificacion(){

    $('#form-modificacion').submit(function (event) {
    
        var $this = $(this);
        var frmValues = $this.serialize();
        
        $.ajax({
            method: "POST",
            url: "/cgi-bin/modificacion.py",
            data: frmValues
        })
        .done(function (res) {
            $('#success-msg').html(res);
            $('#alertSuccess').removeAttr("hidden");
        })
        .fail(function (err) {
            
            $('#error-msg').html(err.responseText);
            $('#alertError').removeAttr("hidden");
        });
        event.preventDefault(); 
    });
}