function send_message(){
    var mensaje = document.getElementById("input_chat").value;
    console.log(mensaje);
    document.getElementById("input_chat").value = "";
    // Mostrar el mensaje en el chat con el nick del usuario para distinguir el mensaje
    
}