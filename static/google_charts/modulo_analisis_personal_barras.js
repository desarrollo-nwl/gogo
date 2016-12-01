google.load("visualization", "1", {packages:["corechart"]});
google.setOnLoadCallback(drawChartPersonal);

function drawChartPersonal() {
  var data = google.visualization.arrayToDataTable([
    ['Dimenciones', 'Promedio Nacional', 'Promedio Colaborador'],
    ['Engagement',  5.40, 4.50],
    ['Team Power',  4.70, 3.67],
    ['Leadership',  3.60, 4.50],
    ['Bussiness Strategy',  4.60, 4.50],
    ['Employer branding',  5.30, 4.30]
  ]);

  var options = {

	legend: {position: 'top', maxLines: 1,'alignment':'center'},

 };

var chart = new google.visualization.ColumnChart(document.getElementById('modulo_analisis_personal_barras'));
  chart.draw(data, options);
}

$(document).ready(function() {
	$(window).resize(function() {
		drawChartPersonal();
	});
});
