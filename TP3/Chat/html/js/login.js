function login(){
    
    var container = $("#frame")

    $('#form-login').submit(function (event) {
    
        var $this = $(this);
        var frmValues = $this.serialize();
        
        $.ajax({
            method: "POST",
            url: "/cgi-bin/login.py",
            data: frmValues
        })
        .done(function (res) {
            container.html(res);
            location.href = "/"
        })
        .fail(function (err) {
            console.log(err);
        });
        event.preventDefault(); 
    });
}