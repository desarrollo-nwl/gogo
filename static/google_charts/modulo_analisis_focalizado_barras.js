google.load("visualization", "1", {
	packages : ["corechart"]
});
google.setOnLoadCallback(drawChartUno);

function drawChartUno() {
	var data = google.visualization.arrayToDataTable([['Dimensiones', 'Tot Desacuerdo', 'Parcialmente Desacuerdo', 'Neutral', 'Parcialmente de acuerdo', 'Totalmente de acuerdo'], ['Regional Norte', 55.40, 60.60, 70.40, 50.80, 8.80], ['Regional Centro', 40.70, 89.23, 25.10, 10.50, 90.47], ['Regional Sur', 60.50, 40.60, 90.50, 70.60, 40.80], ['Regional Oriente', 59.65, 50.44, 80.10, 63.30, 60.51], ['Regional Occidente', 12.30, 16.80, 25.80, 22.30, 22.80]]);

	var options = {

		legend:{ position: 'top', maxLines: 3, 'alignment':'center'},
		vAxis : {
			maxValue : 100,
			minValue : 0
		},

	};

	var chart = new google.visualization.ColumnChart(document.getElementById('modulo_ocho_barras'));
	chart.draw(data, options);
}


$(document).ready(function() {
	$(window).resize(function() {
		drawChartUno();
	});
});
