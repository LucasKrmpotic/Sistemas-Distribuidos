function get_alta() {
    container = $('#main-container')

    $.ajax({
      method: "GET",
      url: "/cgi-bin/alta.py"
    })
    .done(function (res) {
      container.html(res);
    })
    .fail(function (err) {
      alert("error");
      console.log(err);
      
    })
}