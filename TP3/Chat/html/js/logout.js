function logout(){
        
    $.ajax({
        method: "POST",
        url: "/cgi-bin/logout.py"
    })
    .done(function (res) {
        location.href = "/"
    })
    .fail(function (err) {
        console.log(err);
        
    });

}