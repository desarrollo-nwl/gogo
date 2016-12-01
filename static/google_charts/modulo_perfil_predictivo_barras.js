google.load("visualization", "1", {packages:["corechart"]});
google.setOnLoadCallback(drawChartUno);

function drawChartUno() {
  var data = google.visualization.arrayToDataTable([
    ['Dimenciones', 'Promedio Nacional', 'Promedo Filtro'],
    ['Employer Branding',  5.40, 4.50],
    ['Business Strategy',  4.70, 3.67],
    ['Leadership',  3.60, 4.50],
    ['Team Power',  4.60, 4.50],
    ['Engagement',  5.30, 4.30]
  ]);

  var options = {

	legend: {position: 'top', maxLines: 3,'alignment':'center'},

 };

var chart = new google.visualization.ColumnChart(document.getElementById('modulo_perfil_predictivo_barras'));
  chart.draw(data, options);
}

$(document).ready(function() {
	$(window).resize(function() {
		drawChartUno();
	});
});
