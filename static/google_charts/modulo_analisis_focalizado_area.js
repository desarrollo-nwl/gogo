google.setOnLoadCallback(drawChart);
	function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['Year', 'Tot Desacuerdo', 'Parcialmente Desacuerdo', 'Neutral', 'Parcialmente de acuerdo', 'Totalmente de acuerdo'],
          ['ene. 2016',  1000, 400, 300, 500, 200],
          ['feb. 2016',  1170, 460, 200, 300, 200],
          ['mar. 2016',  660, 1120, 300, 250, 300],
          ['abril. 2016',  1030, 540, 100, 600, 700]
        ]);

		var options = {
          isStacked: 'relative',
          height: 300,
          legend: {position: 'top', maxLines: 3, 'alignment':'center'},
          vAxis: {
            minValue: 0,
            ticks: [0, .3, .6, .9, 1]
          }
		};

		        var options_fullStacked = {
          isStacked: 'relative',
          height: 300,
          legend: {position: 'top', maxLines: 3, 'alignment':'center'},
          vAxis: {
            minValue: 0,
            ticks: [0, .3, .6, .9, 1]
          }
        };


		var chart = new google.visualization.AreaChart(document.getElementById('modulo_ocho_area'));
		chart.draw(data, options);
	}
