$( document ).ready(function(){
    
    main();
    function main(){
        var container = $("#frame")
        $.ajax({
            method: "GET",
            url: "/cgi-bin/main.py",
        })
        .done(function (res) {
            container.html(res);
        })
        .fail(function (err) {
            container.html(err);
        }); 
    }

    var interval = null;

    let cookie = Cookies.get('session');

    if (typeof cookie === "undefined"){
        clearInterval(interval);
    } else {       
        interval = setInterval(updateChat, 2000);
    }

    function updateChat(){
        
        update_messajes();
        update_users();
    
    }

    function update_messajes(){

        $.ajax({   
            method: "GET",
            url: "/cgi-bin/messages.py",
        })
        .done(function (res) {
            
            $("#lista-mensajes").append(res);
            $(".messages").animate({ scrollTop: $(document).height() }, "fast");
        })
        .fail(function (err) {
            console.log(err);
            
        }); 
        return true;
    }
    
    function update_users(){
        $.ajax({
            method: "GET",
            url: "/cgi-bin/users.py",
        })
        .done(function (res) {
            $("#users-list").html(res);
        })
        .fail(function (err) {
            console.log(err);
        });    
    }
})
