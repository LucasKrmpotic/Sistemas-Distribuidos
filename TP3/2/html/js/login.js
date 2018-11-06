function login(){

    $('#form-login').submit(function (event) {
    
        var $this = $(this);
        var frmValues = $this.serialize();
        
        $.ajax({
            method: "POST",
            url: "/cgi-bin/login.py",
            data: frmValues
        })
        .done(function (res) {
            $('#success-msg').html(res);
            $('#alertSuccess').removeAttr("hidden");

            $("#login").fadeOut();
            $("#logout").fadeIn();
        })
        .fail(function (err) {
            console.log(err);
            
            $('#error-msg').html(err.responseText);
            $('#alertError').removeAttr("hidden");
        });
        event.preventDefault(); 
    });
}

function get_login(){
    container = $('#main-container')

    $.ajax({
        method: "GET",
        url: "/cgi-bin/login.py",
    })
    .done(function (res) {

        container.html(res);
    })
    .fail(function (err) {
        $('#error-msg').html(err.responseText);
        $('#alertError').removeAttr("hidden");
    });   
}