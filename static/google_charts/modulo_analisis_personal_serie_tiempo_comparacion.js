google.load('visualization', '1', {
	packages : ['corechart', 'line']
});
google.setOnLoadCallback(drawChart);

function drawChart() {
    var data = new google.visualization.DataTable();
    data.addColumn('date', 'Fecha');
    data.addColumn('number', '10% superior');
    data.addColumn('number', '10% inferior');
    data.addColumn('number', 'Promedio');

    // add 100 rows of pseudo-random-walk data
 	for (var i = 0,
	    val1 = 50,
	    val2 = 50,
	    val3 = 50; i < 100; i++) {
		val1 += (Math.random() * 5) * Math.pow(-1, ~~(Math.random() * 2));
		val2 += (Math.random() * 5) * Math.pow(-1, ~~(Math.random() * 2));
		val3 += (Math.random() * 5) * Math.pow(-1, ~~(Math.random() * 2));

		if (val1 < 0) {
			val1 += 5;
		}
		if (val1 > 100) {
			val1 -= 5;
		}

		if (val2 < 0) {
			val2 += 5;
		}
		if (val2 > 100) {
			val2 -= 5;
		}

		if (val3 < 0) {
			val3 += 5;
		}
		if (val3 > 100) {
			val3 -= 5;
		}

		data.addRow([new Date(2016, 0, i + 1), val1, val2, val3]);
	}

	var options = {
		legend:{ position: 'top', maxLines: 3, 'alignment':'center'},
		series : {
			1 : {
				curveType : 'function'
			}
		}
	};

	var chart = new google.visualization.LineChart(document.getElementById('serie_tiempo_comparacion'));
	chart.draw(data, options);
}

$(document).ready(function() {
	$(window).resize(function() {
		drawChart();
	});
});
