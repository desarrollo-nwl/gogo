/*google.load('visualization', '1', {packages: ['corechart', 'line']});*/
google.load("visualization", "1", {packages:["corechart"], callback: drawChart});
/*google.load("visualization", "1", {"callback" : drawChart});*/
google.setOnLoadCallback(drawBackgroundColor);

var data_json = "[[1443226500000, 60], [1443233700000, 40], [1443244500000, 50], [1443255300000, 60], [1443267900000, 60], [1443278700000, 60], [1443287700000, 60], [1443298500000, 55], [1443309300000, 60], [1443317400000, 60], [1443321900000, 28], [1443325500000, 25], [1443326400000, 60], [1443338100000, 40], [1443349800000, 60], [1443349800000, 60], [1443359700000, 60], [1443359700000, 60], [1443369600000, 60], [1443382200000, 80], [1443393000000, 85], [1443400200000, 40], [1443409200000, 75], [1443420000000, 60]]";
function drawBackgroundColor() {
      var data = new google.visualization.DataTable();
      data.addColumn('date', 'Date');
      data.addColumn('number', 'Formula');
	
      var idata = JSON.parse(data_json);
      for(var i in idata){
          idata[i][0] = new Date(idata[i][0]);
          console.log(idata[i]);
      }
      data.addRows(idata);

      var options = {
        legend: { position: 'none' },
        backgroundColor: '#ffffff'
      };

      var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
      chart.draw(data, options);
    }

$(document).ready(function() {
	$(window).resize(function() {
		drawChart();
	});
}); 