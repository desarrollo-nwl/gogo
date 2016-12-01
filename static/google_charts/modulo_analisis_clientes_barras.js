google.load("visualization", "1", {
	packages : ["corechart"]
});
google.setOnLoadCallback(drawChartUno);

function drawChartUno() {
	var data = google.visualization.arrayToDataTable([['Dimensiones', 'Tot Desacuerdo', 'Parcialmente Desacuerdo', 'Neutral', 'Parcialmente de acuerdo', 'Totalmente de acuerdo'], ['Cliente 1', 55.40, 65.60, 45.40, 70.80, 90.80], ['Cliente 2', 80.70, 19.23, 85.10, 70.50, 14.47], ['Cliente 3', 95.50, 90.60, 84.50, 50.60,70.80], ['Cliente 4', 99.65, 65.44, 83.10, 75.30, 76.51], ['Cliente 5', 75.30, 95.80, 65.80, 72.30, 62.80]]);

	var options = {

		legend:{ position: 'top', maxLines: 3, 'alignment':'center'},
		vAxis : {
			maxValue : 100,
			minValue : 0
		},

	};

	var chart = new google.visualization.ColumnChart(document.getElementById('modulo_clientes_barras'));
	chart.draw(data, options);
}


$(document).ready(function() {
	$(window).resize(function() {
		drawChartUno();
	});
});
