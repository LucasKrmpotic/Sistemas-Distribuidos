function post_login(){
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
        })
        .fail(function (err) {
            console.log(err);
            
            $('#error-msg').html(err.responseText);
            $('#alertError').removeAttr("hidden");
        });
        event.preventDefault(); 
    });
}