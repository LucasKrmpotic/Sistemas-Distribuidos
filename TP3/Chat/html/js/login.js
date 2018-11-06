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
            alert(res);
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


    $("#btn_send").removeAttribute("disabled");
    $("#input_chat").removeAttribute("disabled");
    $("#nick_panel").innerText = nickname;
    $("#cerrarModal").click();

    
    // Refresca el chat cada 2 segundos  
    id = setInterval(function(){ actualizar_chat(); }, 1500);

    // Armar y guardar la cookie
}