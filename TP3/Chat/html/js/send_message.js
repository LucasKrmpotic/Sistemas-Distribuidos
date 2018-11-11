function send_message(){
    $("#form-msg").submit(function (event){
    
        var $this = $(this);
        var frmValues = $this.serialize();

        $.ajax({
            method: "POST",
            url: "/cgi-bin/messages.py",
            data: frmValues
        })
        .done(function (res) {
    
            // $("#lista-mensajes").html(res);
            $('.message-input input').val(null);
            // $(".messages").animate({ scrollTop: $(document).height() }, "fast");
        })
        .fail(function (err) {
    
            console.log(err);
        });  
    
        event.preventDefault(); 
    
    });
}
