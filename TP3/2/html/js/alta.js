function get_alta() {
    container = $('#main-container')

    $.ajax({
      method: "GET",
      url: "/cgi-bin/alta.py"
    })
    .done(function (res) {
      container.html(res)
    })
    .fail(function (err) {
        $('#error-msg').html(err.responseText);
        $('#alertError').removeAttr("hidden");
    });
}

function post_alta(){
    
  $('#form-alta').submit(function (event) {
  
      var $this = $(this);
      var frmValues = $this.serialize();
      
      $.ajax({
          method: "POST",
          url: "/cgi-bin/alta.py",
          data: frmValues
      })
      .done(function (res) {
          $('#success-msg').html(res);
          $('#alertSuccess').removeAttr("hidden");
      })
      .fail(function (err) {
          console.log(err);
          
          $('#error-msg').html(err.responseText);
          $('#alertError').removeAttr("hidden");
      });
      event.preventDefault(); 
  });
}