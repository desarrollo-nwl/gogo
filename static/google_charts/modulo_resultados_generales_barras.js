google.load("visualization", "1", {
	packages : ["corechart"]
});
google.setOnLoadCallback(drawChartBarras);

function drawChartBarras() {
	var data = google.visualization.arrayToDataTable([['Dimensiones', 'Promedio Nacional'],['Employer Branding',3.50], ['Business Strategy', 6.40], ['Leadership', 4.70], ['Team Power', 3.60], ['Engagement', 4.60], ]);

	var options = {

		legend : 'none',
		vAxis : {
			maxValue : 10,
			minValue : 0
		},

	};

	var chart = new google.visualization.ColumnChart(document.getElementById('barras'));
	chart.draw(data, options);
}


$(document).ready(function() {
	$(window).resize(function() {
		drawChartBarras();
	});
});
