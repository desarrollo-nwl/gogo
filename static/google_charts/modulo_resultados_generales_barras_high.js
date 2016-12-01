google.load('visualization', '1', {packages:['corechart', 'bar']});
google.setOnLoadCallback(drawChartBarrasHigh);

function drawChartBarrasHigh() {
      var data = google.visualization.arrayToDataTable([
        ['Element', 'Density', { role: 'style' } ],
         ['Conciencia',8.50, '#b87333'],
         ['Compromiso', 9.40, 'silver'],
         ['Conocimiento', 8.70, 'gold'],
         ['Gestión de Procecos', 8.60, '#01DF01'],
         ['Orientación al Logro', 7.60, 'blue'],
         ['Flexibilidad', 8.30, '#8A2908'],
      ]);

      var view = new google.visualization.DataView(data);
      view.setColumns([0, 1,
                       { calc: 'stringify',
                         sourceColumn: 1,
                         type: 'string',
                         role: 'annotation' },
                       2]);

      var options = {
        title: '10% Superior ',
        bar: {groupWidth: '95%'},
        legend: { position: 'none' },
        vAxis : {
			maxValue: 10,
			minValue: 0
		},
      };
      var chart = new google.visualization.ColumnChart(document.getElementById('barras_high'));
      chart.draw(view, options);
  }

$(document).ready(function () {
    $(window).resize(function(){
        drawChartBarrasHigh();
    });
});
