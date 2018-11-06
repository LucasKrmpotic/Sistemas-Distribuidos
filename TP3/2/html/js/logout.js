function logout(){

    $.ajax({
        method: "POST",
        url: "/cgi-bin/logout.py"
    })
    .done(function (res) {
        $('#success-msg').html(res);
        $('#alertSuccess').fadeIn();

        $("#login").fadeIn();
        $("#logout").fadeOut();

        location.href = "/"
    })
    .fail(function (err) {
        
        $('#error-msg').html(err.responseText);
        $('#alertError').fadeIn();

    }); 

}