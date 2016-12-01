      google.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = google.visualization.arrayToDataTable([
            ['MAC', '10% Superior', '10% inferior', {type: 'string', role: 'tooltip'}],
            [ 3.5, 75.54, null, 'Julian Alvarado'],
            [ 4.8, 81.56, null, 'Marcela Carvajal'],
            [ 4.9, 59.34, null, 'Ricardo Gutierrez'],
            [ 5.8, 75.34, null, 'Angela Rodriguez'],
            [ 3.8, null, 34.54, 'Andrea Giraldo'],
            [ 5.5, null, 29.45, 'Lucas Jaramillo']
        ]);

        var options = {
          hAxis: {title: 'Medición', minValue: 0, maxValue: 5},
          vAxis: {title: 'KPI', minValue: 0, maxValue: 100},
          legend: {position: 'top', maxLines: 3, 'alignment':'center'}
        };

        var chart = new google.visualization.ScatterChart(document.getElementById('comparacion_scatter'));

        chart.draw(data, options);
      }

$(document).ready(function() {
	$(window).resize(function() {
		drawChart();
	});
});
