function login(){
 
    var nickname = $("#input_login").value;

    $('#form-login').submit(function (event) {
    
        var $this = $(this);
        var frmValues = $this.serialize();
        
        $.ajax({
            method: "POST",
            url: "/cgi-bin/login.py",
            data: frmValues
        })
        .done(function (res) {
            
            location.href = "/"

        })
        .fail(function (err) {
            console.log(err);
            
        });
        event.preventDefault(); 
    });

}