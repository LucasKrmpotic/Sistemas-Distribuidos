function readCookie(name) {
    var nameEQ = encodeURIComponent(name) + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) === ' ')
            c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) === 0)
            return decodeURIComponent(c.substring(nameEQ.length, c.length));
    }
    return null;
}


$( document ).ready(function(){
    let cookie = readCookie('session')
    
    if (cookie == null){
        $("#login").fadeIn();
        $("#logout").fadeOut();    
    } else {
        $("#login").fadeOut();
        $("#logout").fadeIn();
    }
})