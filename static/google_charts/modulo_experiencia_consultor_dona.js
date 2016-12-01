google.charts.load("current", {
	packages : ["corechart"]
});
google.charts.setOnLoadCallback(drawChart);
function drawChart() {
	var data = google.visualization.arrayToDataTable([['Estado', 'Cantidad'], ['Realizados', 11], ['Ejecución', 2], ['Sin Iniciar', 2]]);

	var options = {
		legend: {position: 'top', maxLines: 1,'alignment':'center'},
		pieHole : 0.2,
	};

	var chart = new google.visualization.PieChart(document.getElementById('donutchart'));
	chart.draw(data, options);
}