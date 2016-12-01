google.setOnLoadCallback(drawChart);
function drawChart() {
	var data = google.visualization.arrayToDataTable([['Year', 'Positivo', 'Neutral', 'Negativo'], ['2013', 1000, 400, 300], ['2014', 1170, 460, 200], ['2015', 660, 1120, 300], ['2016', 1030, 540, 100]]);

	var options = {
		isStacked : 'relative',
		height : 300,
		legend : {
			position : 'top',
			maxLines : 3
		},
		colors : ['#73B148', '#eeebee', '#c42637'],
		vAxis : {
			minValue : 0,
		}
	};

	var options_fullStacked = {
		isStacked : 'relative',
		height : 300,
		legend : {
			position : 'top',
			maxLines : 3
		},
		vAxis : {
			minValue : 0,
			ticks : [0, .3, .6, .9, 1]
		}
	};

	var chart = new google.visualization.AreaChart(document.getElementById('modulo_sentiment'));
	chart.draw(data, options);
}


$(document).ready(function() {
	$(window).resize(function() {
		drawChart();
	});
}); 