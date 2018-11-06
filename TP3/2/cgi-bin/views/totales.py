def table_totales(table_body):

	return """
<div class="container">
<div class="row justify-content-md-center">
    <div class="col-md-8">
    <h2 style="text-align: center; margin-top:1em;">Totales por sexo y grupo etario</h2>
    </div>
</div>
<div class="row justify-content-md-center">
<div class="col-md-10">
<table class="table table-hover" style="margin-top:1em;">
  <thead>
    <tr>
      <th scope="col">Sexo</th>
      <th scope="col">[0..20]</th>
      <th scope="col">[21..40]</th>
      <th scope="col">[41..]</th>
    </tr>
  </thead>
  <tbody>{}</tbody>
        </table>
        </div>
        </div>
        </div>
""".format(table_body)