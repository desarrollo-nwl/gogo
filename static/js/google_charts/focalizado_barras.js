google.load("visualization", "1", {packages:["corechart"]});
google.setOnLoadCallback(drawChartUno);

function drawChartUno() {
  var data = google.visualization.arrayToDataTable([
    ['Dimensiones', 'R1', 'R2', 'R3', 'R4', 'R5'],
    ['Area 1',  5.40,  5.40,  5.40,  5.40,  5.40],
    ['Area 2',  30.70,  30.70,  30.70,  30.70,  30.70],
    ['Area 3',  40.60,  40.60,  40.60,  40.60,  40.60],
    ['Area 4',  20.00,  20.00,  20.00,  20.00,  20.00],
    ['Area 5',  3.30,  3.30,  3.30,  3.30,  3.30]
  ]);

  var options = {

	legend: 'none',

 };

var chart = new google.visualization.ColumnChart(document.getElementById('modulo_ocho_barras'));
  chart.draw(data, options);
}

$(document).ready(function() {
	$(window).resize(function() {
		drawChartUno();
	});
});