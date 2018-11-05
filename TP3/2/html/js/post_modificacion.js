function post_modificacion(){

    $('#form-modificacion').submit(function (event) {
    
        var $this = $(this);
        var frmValues = $this.serialize();
        console.log(frmValues);
        
        $.ajax({
            method: "POST",
            url: "/cgi-bin/modificacion.py",
            data: frmValues
        })
        .done(function (res) {
            console.log(res);
            $('#success-msg').html(res);
            $('#alertSuccess').removeAttr("hidden");
        })
        .fail(function (err) {
            console.log(err);
            
            $('#error-msg').html(err.responseText);
            $('#alertError').removeAttr("hidden");
        });
        event.preventDefault(); 
    });
}