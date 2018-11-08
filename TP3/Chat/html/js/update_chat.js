function update_chat(){
    
    $.ajax({
        method: "GET",
        url: "/cgi-bin/messages.py",
    })
    .done(function (res) {

        console.log(res)
    })
    .fail(function (err) {

        console.log(err);
        

    });   

};