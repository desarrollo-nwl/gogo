google.charts.load("current", {
	packages : ["corechart"]
});
google.charts.setOnLoadCallback(drawChartOne);
function drawChartOne() {
	var data = google.visualization.arrayToDataTable([['Estado', 'Cantidad'], ['Ganadas', 11], ['Canjeadas', 2]]);

	var options = {
		legend: {position: 'top', maxLines: 1,'alignment':'center'},
		pieHole : 0.2,
	};

	var chart = new google.visualization.PieChart(document.getElementById('donutchart_millas_gastadas'));
	chart.draw(data, options);
}

google.charts.setOnLoadCallback(drawChart);
function drawChart() {
	var data = google.visualization.arrayToDataTable([['Estado', 'Cantidad'], ['Calidad de Vida', 11], ['Productividad', 2], ['Bienestar y Recreación', 7]]);

	var options = {
		legend: {position: 'top', maxLines: 1,'alignment':'center'},
		pieHole : 0.2,
	};

	var chart = new google.visualization.PieChart(document.getElementById('donutchart_millas_canjeadas'));
	chart.draw(data, options);
}
