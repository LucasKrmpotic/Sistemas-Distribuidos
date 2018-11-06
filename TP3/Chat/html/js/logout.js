function log_out(){
    document.getElementById("btn_send").setAttribute("disabled", true);
    document.getElementById("input_chat").setAttribute("disabled", true);
    document.getElementById("nick_panel").innerText = "Nick";
    
    // Quitar los contactos de la cajita
    
    document.getElementById("input_chat").value = "";
    
    // Limpiar el chat

    clearInterval(id);
}