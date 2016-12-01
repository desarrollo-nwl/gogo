google.charts.load('current', {packages: ['corechart', 'bar']});
google.charts.setOnLoadCallback(drawAxisTickColors);

function drawAxisTickColors() {
      var data = google.visualization.arrayToDataTable([
        ['Variable', 'Hombres', 'Mujeres'],
        ['Nivel Academico', 3, 5],
        ['Estado Civil - Soltero', 3, 5],
        ['Estado Civil - Casado', 4, 4],
        ['Estado Civil - Divorciado', 4, 4],
        ['Edad', 4, 3]
      ]);

      var options = {
        chartArea: {width: '50%'},
        legend:{ position: 'top', maxLines: 3, 'alignment':'center'},
        hAxis: {
          minValue: 0,
          textStyle: {
            bold: true,
            fontSize: 10,
            color: '#4d4d4d'
          },
          titleTextStyle: {
            bold: true,
            fontSize: 10,
            color: '#4d4d4d'
          }
        },
        vAxis: {
          textStyle: {
            fontSize: 10,
            bold: true,
            color: '#848484'
          },
          titleTextStyle: {
            fontSize: 10,
            bold: true,
            color: '#848484'
          }
        }
      };
      var chart = new google.visualization.BarChart(document.getElementById('modulo_perfil_predictivo_barras_hor'));
      chart.draw(data, options);
    }