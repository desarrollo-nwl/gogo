function drawChart() {
	var data = new google.visualization.DataTable();
	data.addColumn('number', 'X');
	data.addColumn('number', 'Conocimiento Estratégico');
	data.addColumn('number', 'Planeación');
	data.addColumn('number', 'Abordaje');
	data.addColumn('number', 'Solución');
	data.addColumn('number', 'Compromiso y cierre');
	data.addColumn('number', 'Retención y lealtad');
	data.addColumn('number', 'Comportamientos Transversales');


	data.addRows([
		[0, 0, 0, 0, 0, 0, 0, 0], 
		[1, 3.8, 4, 4.8, 3.6, 7.5, 1.4, 6.7], 
		[2, 3.8, 4.1, 5, 3.2, 6.5, 2.4, 5.7 ], 
		[3, 3.7, 4.1, 5, 3.6, 7.8, 1.6, 4.7], 
		[4, 3.6, 4.2, 4.5, 3.6, 7.7, 4.4, 6.5], 
		[5, 3.4, 4.1, 5.0, 3.6, 7.9, 3.4, 5.7], 
		[6, 3.8, 4.0, 5.0, 3.6, 6.5, 3.5, 4.8], 
		[7, 3.6, 4.0, 4.7, 3.6, 5.5, 7.4, 4.9], 
		[8, 3.6, 4.1, 5.0, 3.6, 7.7, 1.4, 5.1], 
		[9, 3.7, 3.9, 3.9, 3.6, 4.5, 5.4, 6.4], 
		[10, 4.0, 4.3, 4.5, 3.6, 5.5, 6.4, 5.5], 
		[11, 4.2, 4.2, 5.0, 3.6, 6.4, 1.4, 6.2], 
		[12, 4.1, 4.1, 4.9, 3.6, 5.5, 6.4, 5.8], 
		[13, 4.1, 4.1, 4.7, 3.6, 8.4, 2.8, 7.2], 
		[14, 4.2, 4.1, 4.6, 3.6, 7.5, 6.4, 5.6], 
		[15, 4.0, 4.2, 4.8, 3.6, 3.8, 8.2, 2.9], 
		[16, 4.0, 4.2, 4.7, 3.6, 6.5, 9.1, 3.5], 
		[17, 4.0, 4.2, 4.6, 3.6, 8.4, 6.7, 6.4], 
		[18, 4.1, 4.1, 4.3, 3.6, 8.4, 7.8, 2.8], 
		[19, 4.1, 4.2, 4.3, 3.6, 5.9, 6.5, 6.4], 
		[20, 4.0, 3.9, 4.8, 3.6, 4.5, 6.7, 5.2]
		]);
    
    var chart = new google.visualization.ChartWrapper({
        chartType: 'LineChart',
        containerId: 'chart_div',
        options: {
            height: 200,
            // omit width, since we set this in CSS
            legend: 'none',
            colors: ['#e2431e', '#f1ca3a', '#6f9654', '#1c91c0','#4374e0'],
            chartArea: {
                width: '80%' // this should be the same as the ChartRangeFilter
            }
        }
    });
    
    var control = new google.visualization.ControlWrapper({
        controlType: 'ChartRangeFilter',
        containerId: 'control_div',
        options: {
            filterColumnIndex: 0,
            ui: {
                chartOptions: {
                    height: 50,
                    // omit width, since we set this in CSS
                    colors: ['#e2431e', '#f1ca3a', '#6f9654', '#1c91c0','#4374e0'],
                    chartArea: {
                        width: '80%' // this should be the same as the ChartRangeFilter
                    }
                }
            }
        }
    });
    
    var dashboard = new google.visualization.Dashboard(document.querySelector('#dashboard_div'));
    dashboard.bind([control], [chart]);
    dashboard.draw(data);
    
    function zoomLastDay () {
        var range = data.getColumnRange(0);
        control.setState({
            range: {
                start: new Date(range.max.getFullYear(), range.max.getMonth(), range.max.getDate() - 1),
                end: range.max
            }
        });
        control.draw();
    }
    function zoomLastWeek () {
        var range = data.getColumnRange(0);
        control.setState({
            range: {
                start: new Date(range.max.getFullYear(), range.max.getMonth(), range.max.getDate() - 7),
                end: range.max
            }
        });
        control.draw();
    }
    function zoomLastMonth () {
        // zoom here sets the month back 1, which can have odd effects when the last month has more days than the previous month
        // eg: if the last day is March 31, then zooming last month will give a range of March 3 - March 31, as this sets the start date to February 31, which doesn't exist
        // you can tweak this to make it function differently if you want
        var range = data.getColumnRange(0);
        control.setState({
            range: {
                start: new Date(range.max.getFullYear(), range.max.getMonth() - 1, range.max.getDate()),
                end: range.max
            }
        });
        control.draw();
    }
    
    var runOnce = google.visualization.events.addListener(dashboard, 'ready', function () {
        google.visualization.events.removeListener(runOnce);
        
        if (document.addEventListener) {
            document.querySelector('#lastDay').addEventListener('click', zoomLastDay);
            document.querySelector('#lastWeek').addEventListener('click', zoomLastWeek);
            document.querySelector('#lastMonth').addEventListener('click', zoomLastMonth);
        }
        else if (document.attachEvent) {
            document.querySelector('#lastDay').attachEvent('onclick', zoomLastDay);
            document.querySelector('#lastWeek').attachEvent('onclick', zoomLastWeek);
            document.querySelector('#lastMonth').attachEvent('onclick', zoomLastMonth);
        }
        else {
            document.querySelector('#lastDay').onclick = zoomLastDay;
            document.querySelector('#lastWeek').onclick = zoomLastWeek;
            document.querySelector('#lastMonth').onclick = zoomLastMonth;
        }
    });
}
google.load('visualization', '1', {packages:['controls'], callback: drawChart});

$(document).ready(function() {
	$(window).resize(function() {
		drawChart();
	});
});