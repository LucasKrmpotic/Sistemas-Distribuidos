// $(window).on('keydown', function (e) {
//     if (e.which == 13) {
//         if ( URLActual != 'http://localhost:8080/login.html'){
//             newMessage();
//         }else{
//             location.href = "/"
//         }
//         return false;
//     }
// });


// $('#btn-send').click(function () {
//     newMessage();
// });

function newMessage() {
    // message = $(".message-input input").val();
    // if ($.trim(message) == '') {
    //     return false;
    // }

    $("#form-msg").submit(function (event){

        var $this = $(this);
        var frmValues = $this.serialize();
        
        console.log(frmValues);
        $.ajax({
            method: "POST",
            url: "/cgi-bin/messages.py",
            data: frmValues
        })
        .done(function (res) {
    
            console.log(res)
        })
        .fail(function (err) {
    
            console.log(err);
        });  

        event.preventDefault(); 

    });


    // $('<li class="sent"><img src="http://emilcarlsson.se/assets/mikeross.png" alt="" /><p>' + message + '</p></li>').appendTo($('.messages ul'));
    // $('.message-input input').val(null);
    // $('.contact.active .preview').html('<span>You: </span>' + message);
    // $(".messages").animate({ scrollTop: $(document).height() }, "fast");
};