google.load('visualization', '1', {packages:['corechart', 'bar']});
google.setOnLoadCallback(drawChartBarrasLow);

function drawChartBarrasLow() {
      var data = google.visualization.arrayToDataTable([
        ['Element', 'Density', { role: 'style' } ],
        ['Autogestión',3.50, '#b87333'],
        ['Interacción', 6.40, 'silver'],
        ['Influencia', 4.70, 'gold'],
        ['Gestión de Procecos', 3.60, '#01DF01'],
        ['Orientación al Logro', 4.60, 'blue'],
        ['Flexibilidad', 5.30, '#8A2908'],
      ]);

      var view = new google.visualization.DataView(data);
      view.setColumns([0, 1,
                       { calc: 'stringify',
                         sourceColumn: 1,
                         type: 'string',
                         role: 'annotation' },
                       2]);

      var options = {
        title: '10% Inferior ',
        bar: {groupWidth: '95%'},
        legend: { position: 'none' },
        vAxis : {
			maxValue: 10,
			minValue: 0
		},
      };
      var chart = new google.visualization.ColumnChart(document.getElementById('barras_low'));
      chart.draw(view, options);
  }

$(document).ready(function () {
    $(window).resize(function(){
        drawChartBarrasLow();
    });
});
