function drawChart() {
	var data = new google.visualization.DataTable();
	data.addColumn('date', 'Fecha');
	data.addColumn('number', 'Promedio Medición');

	// add 100 rows of pseudo-random-walk data
	for (var i = 0,
	    val = 50; i < 100; i++) {
		val += ~~(Math.random() * 5) * Math.pow(-1, ~~(Math.random() * 2));
		if (val < 0) {
			val += 5;
		}
		if (val > 100) {
			val -= 5;
		}
		data.addRow([new Date(2016, 0, i + 1), val]);
	}

	var chart = new google.visualization.ChartWrapper({
		chartType : 'LineChart',
		containerId : 'chart_div',
		options : {
			height : 200,
			// omit width, since we set this in CSS
			legend : 
			{ position: 'top','alignment':'center'
			},
			colors : ['#43AEA8'],
			chartArea : {
				width : '80%' // this should be the same as the ChartRangeFilter
			},
			trendlines : {
				0 : {
					color : 'purple',
					lineWidth : 4,
					opacity : 0.2,
					showR2 : true,
					visibleInLegend : true
				}
			}
		}
	});

	var control = new google.visualization.ControlWrapper({
		controlType : 'ChartRangeFilter',
		containerId : 'control_div',
		options : {
			filterColumnIndex : 0,
			ui : {
				chartOptions : {
					height : 50,
					// omit width, since we set this in CSS
					colors : ['#43AEA8'],
					chartArea : {
						width : '80%' // this should be the same as the ChartRangeFilter
					}
				}
			}
		}
	});

	var dashboard = new google.visualization.Dashboard(document.querySelector('#dashboard_div'));
	dashboard.bind([control], [chart]);
	dashboard.draw(data);

	function zoomLastDay() {
		var range = data.getColumnRange(0);
		control.setState({
			range : {
				start : new Date(range.max.getFullYear(), range.max.getMonth(), range.max.getDate() - 1),
				end : range.max
			}
		});
		control.draw();
	}

	function zoomLastWeek() {
		var range = data.getColumnRange(0);
		control.setState({
			range : {
				start : new Date(range.max.getFullYear(), range.max.getMonth(), range.max.getDate() - 7),
				end : range.max
			}
		});
		control.draw();
	}

	function zoomLastMonth() {
		// zoom here sets the month back 1, which can have odd effects when the last month has more days than the previous month
		// eg: if the last day is March 31, then zooming last month will give a range of March 3 - March 31, as this sets the start date to February 31, which doesn't exist
		// you can tweak this to make it function differently if you want
		var range = data.getColumnRange(0);
		control.setState({
			range : {
				start : new Date(range.max.getFullYear(), range.max.getMonth() - 1, range.max.getDate()),
				end : range.max
			}
		});
		control.draw();
	}

	var runOnce = google.visualization.events.addListener(dashboard, 'ready', function() {
		google.visualization.events.removeListener(runOnce);

		if (document.addEventListener) {
			document.querySelector('#lastDay').addEventListener('click', zoomLastDay);
			document.querySelector('#lastWeek').addEventListener('click', zoomLastWeek);
			document.querySelector('#lastMonth').addEventListener('click', zoomLastMonth);
		} else if (document.attachEvent) {
			document.querySelector('#lastDay').attachEvent('onclick', zoomLastDay);
			document.querySelector('#lastWeek').attachEvent('onclick', zoomLastWeek);
			document.querySelector('#lastMonth').attachEvent('onclick', zoomLastMonth);
		} else {
			document.querySelector('#lastDay').onclick = zoomLastDay;
			document.querySelector('#lastWeek').onclick = zoomLastWeek;
			document.querySelector('#lastMonth').onclick = zoomLastMonth;
		}
	});
}

google.load('visualization', '1', {
	packages : ['controls'],
	callback : drawChart
});

$(document).ready(function() {
	$(window).resize(function() {
		drawChart();
	});
}); 