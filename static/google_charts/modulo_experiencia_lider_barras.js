google.load("visualization", "1", {packages:["corechart"]});
google.setOnLoadCallback(drawChartPersonal);

function drawChartPersonal() {
  var data = google.visualization.arrayToDataTable([
    ['Lider', 'Promedio Por Aréa'],
    ['Gerencia de estrategia',  5.40 ],
    ['Gerencia Administrativa',  4.70],
    ['Gerencia Financiera',  3.60],
    ['Gerencia de Producción',  4.60],
    ['Gerencia Comercial',  5.30]
  ]);

  var options = {

	legend: {position: 'top', maxLines: 1,'alignment':'center'},

 };

var chart = new google.visualization.ColumnChart(document.getElementById('modulo_analisis_lider_barras'));
  chart.draw(data, options);
}

$(document).ready(function() {
	$(window).resize(function() {
		drawChartPersonal();
	});
});
